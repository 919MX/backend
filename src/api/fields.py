from rest_framework import serializers

from helpers.location import geos_location_from_coordinate_string

class LatLngField(serializers.Field):
    """Field is parsed from `{lat},{lng}` string passed in request body,
    and converted to a geos `Point` instance.

    This makes it easy, for example, for a nurse to update their location.

    5 decimal places gives a precision of 1.1m, it's actually overkill:
    http://gis.stackexchange.com/questions/8650/measuring-accuracy-of-latitude-and-longitude
    """
    def to_representation(self, obj):
        return {'lng': round(obj.x, 5), 'lat': round(obj.y, 5)}

    def to_internal_value(self, data):
        if data:
            try:
                location = geos_location_from_coordinate_string(data)
            except:
                raise serializers.ValidationError(
                    'The location string must have the following format: {lat},{lng}')
            return location
