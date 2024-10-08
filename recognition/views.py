from django.shortcuts import render
from recognition.models import PlateEvent, Camera
from django.utils.dateparse import parse_datetime

def search(request):
    query = request.GET.get('query', '')
    camera_id = request.GET.get('camera')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    results = []

    if start_date and end_date:
        start_datetime = parse_datetime(f'{start_date} 00:00:00')
        end_datetime = parse_datetime(f'{end_date} 23:59:59')

        if query:
            results = PlateEvent.objects.filter(
                plate_number__icontains=query,
                recognition_time__range=[start_datetime, end_datetime]
            )

        elif camera_id:
            results = PlateEvent.objects.filter(
                camera_id=camera_id,
                recognition_time__range=[start_datetime, end_datetime]
            )

    cameras = Camera.objects.all()
    #print(cameras)
    return render(request, 'search.html', {'results': results, 'cameras': cameras})
