from django.db import models
from django.utils import timezone

class Camera(models.Model):
    name = models.CharField(max_length=20)
    ip_address = models.GenericIPAddressField()
    added_date = models.DateTimeField(default=timezone.now)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

class PlateEvent(models.Model):
    plate_number = models.CharField(max_length=10)
    recognition_time = models.DateTimeField(default=timezone.now)
    brand = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)

    def __str__(self):
        return self.plate_number
    

