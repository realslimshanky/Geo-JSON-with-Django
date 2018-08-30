from django.contrib.gis.db import models

from geo_json_with_django.base.models import TimeStampedUUIDModel


class ServiceRegion(TimeStampedUUIDModel):
    provider = models.ForeignKey('users.User', on_delete=models.CASCADE)
    name = models.CharField('Service Region Name', max_length=50)
    price = models.FloatField('Service Region Price')
    region_coordinates = models.PolygonField()

    def is_coordinate_inclusive(self, point_object):
        return self.region_coordinates.touches(point_object) or\
            self.region_coordinates.within(point_object) or\
            self.region_coordinates.contains(point_object)

    class Meta:
        ordering = ['region_coordinates']
