from django.core.management.base import BaseCommand
from django.db import connection
from django.utils.timezone import make_aware
from django.utils import timezone
from datetime import datetime
from recognition.models import Camera, PlateEvent

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
            camera1 = Camera.objects.create(
                name='RMZ',
                ip_address='192.168.1.1',
                added_date = make_aware(datetime(2024, 1, 1, 10, 30)),
                latitude=51.519575,
                longitude=31.274302
            )
            camera2 = Camera.objects.create(
                name='ZAZ',
                ip_address='192.168.1.2',
                added_date = make_aware(datetime(2024, 1, 1, 10, 00)),
                latitude=51.514808,
                longitude=31.265930
            )

            PlateEvent.objects.create(
                plate_number='CB3333CX',
                recognition_time=timezone.now(),
                brand='Toyota',
                color='Red',
                camera=camera1
            )
            PlateEvent.objects.create(
                plate_number='CB1234CX',
                recognition_time=timezone.now(),
                brand='Honda',
                color='Blue',
                camera=camera1
            )
            PlateEvent.objects.create(
                plate_number='CB4567CX',
                recognition_time=timezone.now(),
                brand='BMW',
                color='Black',
                camera=camera2
            )
            PlateEvent.objects.create(
                plate_number='CB7777CX',
                recognition_time=timezone.now(),
                brand='Ford',
                color='White',
                camera=camera2
            )
            PlateEvent.objects.create(
                plate_number='007',
                recognition_time=timezone.now(),
                brand='Mercedes',
                color='Silver',
                camera=camera1
            )

            self.stdout.write(self.style.SUCCESS('++++++'))
