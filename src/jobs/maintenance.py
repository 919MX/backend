import json

from django.db.models import Prefetch
from django.db import transaction, connection
from django.utils import timezone

from celery import shared_task

from db.map.models import Action, Donation, Testimonial


def get_status_by_category(action, prefetched=False):
    d = {}

    d['desc'] = bool(action.desc)

    d['dates'] = bool(action.start_date and action.end_date)

    d['progress'] = bool(action.unit_of_measurement) \
        and action.target is not None and action.progress is not None

    d['budget'] = bool(action.budget)

    d['image_count'] = action.image_count

    if prefetched:
        d['testimonials'] = len(action.testimonials)
        d['donations'] = len(action.donations)
        d['verified_donations'] = len(action.verified_donations)
    else:
        d['testimonials'] = len(action.testimonial_set.filter(published=True))
        d['donations'] = len(action.donation_set.filter(approved_by_donor=True, approved_by_org=True))
        d['verified_donations'] = len(action.donation_set.filter(
            approved_by_donor=True, approved_by_org=True, donor__donoruser__isnull=False).distinct()
        )

    return d


def get_score(status_by_category):
    dates = status_by_category.get('dates', False)
    progress = status_by_category.get('progress', False)
    budget = status_by_category.get('budget', False)
    image_count = status_by_category.get('image_count', 0)
    testimonials = status_by_category.get('image_count', 0)
    donations = status_by_category.get('donations', 0)
    verified_donations = status_by_category.get('verified_donations', 0)

    return (image_count + testimonials * 5) * (
        1 if dates else 0 +
        1 if progress else 0 +
        1 if budget else 0 +
        1 if donations > 0 else 0 +
        1 if verified_donations > 0 else 0
    )


def get_level(status_by_category, score):
    desc = status_by_category.get('desc', False)
    progress = status_by_category.get('progress', False)
    budget = status_by_category.get('budget', False)

    if not desc or not progress or not budget:
        return 0
    if score < 40:
        return 1
    return 2


query = """
UPDATE map_action SET modified = %s::timestamptz, status_by_category = %s, score = %s, level = %s WHERE id = %s"""


@shared_task(name='sync_action_transparency')
def sync_action_transparency():
    with transaction.atomic():
        with connection.cursor() as cursor:
            for action in Action.objects.prefetch_related(
                Prefetch('testimonial_set', queryset=Testimonial.objects.filter(
                    published=True
                ), to_attr='testimonials'),
                Prefetch('donation_set', queryset=Donation.objects.filter(
                    approved_by_donor=True, approved_by_org=True
                ), to_attr='donations'),
                Prefetch('donation_set', queryset=Donation.objects.filter(
                    approved_by_donor=True, approved_by_org=True, donor__donoruser__isnull=False
                ).distinct(), to_attr='verified_donations'),
            ):
                status_by_category = {**action.status_by_category, **get_status_by_category(action, prefetched=True)}
                score = get_score(status_by_category)
                level = get_level(status_by_category, score)
                cursor.execute(query, [
                    timezone.now().isoformat(), json.dumps(status_by_category), score, level, action.id]
                )