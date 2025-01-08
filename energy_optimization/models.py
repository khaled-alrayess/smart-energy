from django.db import models

class EnergyConsumption(models.Model):
    device_name = models.CharField(max_length=100)
    energy_consumed = models.FloatField(help_text="الطاقة المستهلكة بالكيلو واط")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device_name} - {self.energy_consumed} kWh"

class EnergySetting(models.Model):
    device_name = models.CharField(max_length=100)
    max_energy_limit = models.FloatField(help_text="الحد الأقصى للطاقة بالكيلو واط")

    def __str__(self):
        return f"{self.device_name} - Limit: {self.max_energy_limit} kWh"
