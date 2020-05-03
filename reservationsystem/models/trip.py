from django.db import models


class Trip(models.Model):
    name = models.CharField(max_length=200)
    bus = models.ForeignKey('reservationsystem.bus', on_delete=models.PROTECT)
    trip_route = models.ForeignKey('reservationsystem.triproute', on_delete=models.PROTECT)
    departure_time = models.DateTimeField('departure time')

    def __str__(self):
        return self.name
