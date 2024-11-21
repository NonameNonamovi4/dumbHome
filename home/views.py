from django.shortcuts import render

from django.shortcuts import render

from devices.models import Device
from temperature.models import Temperature
def home_view(request):
    # Get the current temperature
    temperature = Temperature.objects.first()
    current_temp = temperature.value if temperature else "N/A"

    # Example placeholder for logs (you can replace this with actual data)
    recent_logs = [
        "Motion detected at the front door",
        "Living room light turned on",
        "Temperature updated to 22°C"
    ]

    return render(request, 'home/home.html', {
        'current_temp': current_temp,
        'recent_logs': recent_logs
    })
