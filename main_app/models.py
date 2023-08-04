from django.db import models
from django.urls import reverse

ACTIONS = (("C", "Charged Batteries"), ("G", "Greased"), ("B", "Balanced Prop"))
# Create your models here.




class Battery(models.Model):
    Connector = models.CharField(max_length=10)
    MaH = models.IntegerField()
    Cells = models.IntegerField()

    def __str__(self):
        return self.Connector

    def get_absolute_url(self):


     return reverse('batterys_detail', kwargs={'pk': self.id})
    

class RemoteControlVehicle(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    batterys = models.ManyToManyField(Battery)

    def __str__(self):
        return f"{self.id} - {self.model}"

    def get_absolute_url(self):
        return reverse("batterys_detail", kwargs={"rc_id": self.id})
    
class Maint(models.Model):
    date = models.DateField("Completed Date")
    action = models.CharField(max_length=1, choices=ACTIONS, default=ACTIONS[0][0])
    rc = models.ForeignKey(RemoteControlVehicle, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_action_display()} on {self.date}"