from django.shortcuts import render, get_object_or_404
from .models import Temperature
from .forms import TemperatureForm

def temperature_view(request):
    # Get the first temperature entry or create one
    temperature = Temperature.objects.first()
    if not temperature:
        temperature = Temperature.objects.create()

    if request.method == 'POST':
        form = TemperatureForm(request.POST, instance=temperature)
        if form.is_valid():
            form.save()
    else:
        form = TemperatureForm(instance=temperature)

    return render(request, 'temperature/temperature.html', {'form': form, 'temperature': temperature})
