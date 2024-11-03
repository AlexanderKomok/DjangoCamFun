from django.shortcuts import render
from django.utils.dateparse import parse_datetime
from recognition.models import Camera, PlateEvent

def search(request):
    query = request.GET.get('query', '')
    camera_id = request.GET.get('camera')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    results = []
    cameras = Camera.objects.all()

    if start_date and end_date:
        start_datetime = parse_datetime(f'{start_date} 00:00:00')
        end_datetime = parse_datetime(f'{end_date} 23:59:59')

    if query and not camera_id and not (start_date and end_date):
        results = PlateEvent.objects.filter(plate_number__icontains=query).select_related('camera')

    elif camera_id and not query and not (start_date and end_date):
        results = PlateEvent.objects.filter(camera_id=camera_id).select_related('camera')

    elif query and start_date and end_date:
        results = PlateEvent.objects.filter(
            plate_number__icontains=query,
            recognition_time__range=(start_datetime, end_datetime)
        ).select_related('camera')


    elif camera_id and start_date and end_date:
        results = PlateEvent.objects.filter(
            camera_id=camera_id,
            recognition_time__range=(start_datetime, end_datetime)
        ).select_related('camera')

    elif start_date and end_date and not query and not camera_id:
        results = PlateEvent.objects.filter(
            recognition_time__range=(start_datetime, end_datetime)
        ).select_related('camera')

    return render(request, 'search.html', {'results': results, 'cameras': cameras})
