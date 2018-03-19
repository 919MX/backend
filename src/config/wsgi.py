import os

from django.core.wsgi import get_wsgi_application

from raven.contrib.django.raven_compat.middleware.wsgi import Sentry


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')

application = Sentry(get_wsgi_application())
