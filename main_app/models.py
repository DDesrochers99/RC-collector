from django.db import models
from django.urls import reverse

# Create your models here.

class RemoteControlVehicle(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.id} - {self.model}"

    def get_absolute_url(self):
        return reverse("detail", kwargs={"rc_id": self.id})
