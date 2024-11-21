from django.db import models

class Temperature(models.Model):
    value = models.IntegerField(default=20)  # Default temperature in Celsius

    def __str__(self):
        return f"Temperature: {self.value}°C"
