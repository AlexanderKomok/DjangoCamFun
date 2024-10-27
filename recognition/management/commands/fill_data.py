import random
import string
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django.db import connection
from django.utils.timezone import make_aware

def random_date(start, end):
    return make_aware(start + timedelta(seconds=random.randint(0, int((end - start).total_seconds()))))

def random_ip():
    return f"192.168.1.{random.randint(1, 254)}"

def random_coordinates():
    return round(random.uniform(-90.000000, 90.000000), 6), round(random.uniform(-180.000000, 180.000000), 6)

def random_camera_name():
    return ''.join(random.choices(string.ascii_uppercase, k=3))

def random_plate_number():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        start_date = datetime(2024, 1, 1)
        end_date = datetime(2024, 1, 31)

        with connection.cursor() as cursor:
            for _ in range(10):
                name = random_camera_name()
                ip_address = random_ip()
                added_date = random_date(start_date, end_date)
                latitude, longitude = random_coordinates()

                cursor.execute("""
                    INSERT INTO recognition_camera (name, ip_address, added_date, latitude, longitude)
                    VALUES (%s, %s, %s, %s, %s)
                """, (name, ip_address, added_date, latitude, longitude))

            cursor.execute("SELECT id FROM recognition_camera")
            camera_ids = [row[0] for row in cursor.fetchall()]

            colors = ['Red', 'Blue', 'Green', 'Black', 'White', 'Silver', 'Yellow']
            brands = ['Toyota', 'Honda', 'BMW', 'Ford', 'Mercedes', 'Nissan', 'Chevrolet']

            for _ in range(1000):
                plate_number = random_plate_number()
                recognition_time = random_date(start_date, end_date)
                brand = random.choice(brands)
                color = random.choice(colors)
                camera_id = random.choice(camera_ids)

                cursor.execute("""
                    INSERT INTO recognition_plateevent (plate_number, recognition_time, brand, color, camera_id)
                    VALUES (%s, %s, %s, %s, %s)
                """, (plate_number, recognition_time, brand, color, camera_id))

        self.stdout.write(self.style.SUCCESS('++++++'))
