from django.shortcuts import render
from django.http import JsonResponse
from devices.models import Device

def devices_home(request):
    devices = Device.objects.all()
    return render(request, 'devices/devices.html', {'devices': devices})

def toggle_device(request):
    if request.method == "POST":
        device_id = request.POST.get('id')
        is_on = request.POST.get('is_on') == 'true'
        try:
            device = Device.objects.get(id=device_id)
            device.is_on = is_on
            device.save()
            return JsonResponse({'status': 'success'})
        except Device.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Device not found'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})
