from django import forms
from .models import Temperature

class TemperatureForm(forms.ModelForm):
    class Meta:
        model = Temperature
        fields = ['value']
        widgets = {
            'value': forms.NumberInput(attrs={
                'type': 'range',
                'min': '10',  # Set minimum temperature
                'max': '30',  # Set maximum temperature
                'step': '1',
                'id': 'temperature-slider',
                'oninput': 'updateSliderValue(this.value)',  # JS function to show live updates
            }),
        }
