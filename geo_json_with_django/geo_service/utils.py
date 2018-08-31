from django.contrib.gis.geos import Polygon
from django.contrib.gis.geos.error import GEOSException


def get_polygon_object(coordinates):
        try:
            coordinates = eval(coordinates)
            if type(coordinates) in [list, tuple] and coordinates:
                if coordinates[0] != coordinates[-1]:
                    coordinates.append(coordinates[0])
                return Polygon(coordinates)
            else:
                raise ValueError
        except (SyntaxError, ValueError, TypeError, GEOSException) as e:
                return str(e)
