from django.shortcuts import render
from django.db import connection
from django.utils.dateparse import parse_datetime

def search(request):
    query = request.GET.get('query', '')
    camera_id = request.GET.get('camera')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    results = []
    cameras = []

    with connection.cursor() as cursor:
        cursor.execute("SELECT id, name FROM recognition_camera")
        cameras = cursor.fetchall()

    if start_date and end_date:
        start_datetime = parse_datetime(f'{start_date} 00:00:00')
        end_datetime = parse_datetime(f'{end_date} 23:59:59')
    
    #только номер
    if query and not camera_id and not (start_date and end_date):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT pe.plate_number, pe.brand, pe.color, pe.recognition_time,
                       c.name, c.ip_address, c.latitude, c.longitude
                FROM recognition_plateevent pe
                JOIN recognition_camera c ON pe.camera_id = c.id
                WHERE pe.plate_number ILIKE %s
            """, [f'%{query}%'])
            results = cursor.fetchall()

    #только камера
    elif camera_id and not query and not (start_date and end_date):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT pe.plate_number, pe.brand, pe.color, pe.recognition_time,
                       c.name, c.ip_address, c.latitude, c.longitude
                FROM recognition_plateevent pe
                JOIN recognition_camera c ON pe.camera_id = c.id
                WHERE pe.camera_id = %s
            """, [camera_id])
            results = cursor.fetchall()

    #номер и диапазон дат
    elif query and start_date and end_date:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT pe.plate_number, pe.brand, pe.color, pe.recognition_time,
                       c.name, c.ip_address, c.latitude, c.longitude
                FROM recognition_plateevent pe
                JOIN recognition_camera c ON pe.camera_id = c.id
                WHERE pe.plate_number ILIKE %s
                AND pe.recognition_time BETWEEN %s AND %s
            """, [f'%{query}%', start_datetime, end_datetime])
            results = cursor.fetchall()

    #камера и диапазон дат
    elif camera_id and start_date and end_date:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT pe.plate_number, pe.brand, pe.color, pe.recognition_time,
                       c.name, c.ip_address, c.latitude, c.longitude
                FROM recognition_plateevent pe
                JOIN recognition_camera c ON pe.camera_id = c.id
                WHERE pe.camera_id = %s
                AND pe.recognition_time BETWEEN %s AND %s
            """, [camera_id, start_datetime, end_datetime])
            results = cursor.fetchall()

    #диапазон дат
    elif start_date and end_date and not query and not camera_id:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT pe.plate_number, pe.brand, pe.color, pe.recognition_time,
                       c.name, c.ip_address, c.latitude, c.longitude
                FROM recognition_plateevent pe
                JOIN recognition_camera c ON pe.camera_id = c.id
                WHERE pe.recognition_time BETWEEN %s AND %s
            """, [start_datetime, end_datetime])
            results = cursor.fetchall()

    return render(request, 'search.html', {'results': results, 'cameras': cameras})
