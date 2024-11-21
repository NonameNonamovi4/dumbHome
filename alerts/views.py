from django.shortcuts import render

from django.shortcuts import render


def alerts(request):
    alerts_data = [
        {"type": "Warning", "message": "High temperature detected in Room 1."},
        {"type": "Info", "message": "New device connected: Smart Thermostat."},
        {"type": "Error", "message": "Camera 3 is offline."},
    ]

    return render(request, 'alerts/alerts.html', {"alerts": alerts_data})
