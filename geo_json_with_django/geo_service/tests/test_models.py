# Django Stuff
from django.contrib.gis.geos import Polygon, Point

# Third Party Stuff
from django.test import TestCase

# Geo JSON with Django Stuff
from geo_json_with_django.geo_service.models import ServiceRegion
from geo_json_with_django.users.models import User


class ServiceRegionModelTest(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            email='f@F.com', password='abc', name='FB abc',
            phone_number='+9999999999', language='en', currency='USD')
        ServiceRegion.objects.create(
            provider=user,
            name='Temporary Region',
            price=1000,
            region_coordinates=Polygon([(11.22, 13.11), (22.33, 22.33), (41.11, 42.22), (52.43, 5.22), (11.22, 13.11)])
        )

    def test_region_creation(self):
        service_region = ServiceRegion.objects.all()[0]
        assert str(service_region) == str(service_region.id)

    def test_coordinate_inclusion(self):
        sample_region = ServiceRegion.objects.all()[0]
        coordinate = Point((20, 20))
        assert sample_region.is_coordinate_inclusive(coordinate)
