import os
from django.db import connection
from django.shortcuts import render
from django.conf import settings

def load_sql_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def get_all_cameras():
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, name FROM cameras")
        cameras = cursor.fetchall()
    return cameras

def search(request):
    query = request.GET.get('query', None)
    camera_id = request.GET.get('camera', None)
    start_date = request.GET.get('start_date', None)
    end_date = request.GET.get('end_date', None)

    cameras = get_all_cameras()

    if not query and not camera_id and not start_date and not end_date:
        results = []
    else:
        sql_file_path = os.path.join(settings.BASE_DIR, 'recognition', 'queries', 'get_plate_events.sql')

        sql_query = load_sql_file(sql_file_path)

        query_param = f'%{query}%' if query else None
        camera_param = camera_id if camera_id else None
        start_date_param = start_date if start_date else None
        end_date_param = end_date if end_date else None

        with connection.cursor() as cursor:
            cursor.execute(sql_query, [
                query_param, query_param,
                camera_param, camera_param,
                start_date_param, start_date_param,
                end_date_param, end_date_param
            ])
            rows = cursor.fetchall()

        results = []
        for row in rows:
            results.append({
                'plate_number': row[0],
                'brand': row[1],
                'color': row[2],
                'recognition_time': row[3],
                'camera_name': row[4],
                'ip_address': row[5],
                'latitude': row[6],
                'longitude': row[7],
            })

    return render(request, 'search.html', {'results': results, 'cameras': cameras})
