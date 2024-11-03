from django.db import models

class Camera(models.Model):
    name = models.CharField(max_length=20)
    ip_address = models.CharField(max_length=16)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)

    class Meta:
        db_table = 'cameras'

class PlateEvent(models.Model):
    plate_number = models.CharField(max_length=8)
    brand = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)
    recognition_time = models.DateTimeField()

    class Meta:
        db_table = 'plate_events'