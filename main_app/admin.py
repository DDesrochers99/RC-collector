from django.contrib import admin
from .models import RemoteControlVehicle, Maint, Battery
# Register your models here.

admin.site.register(RemoteControlVehicle)
admin.site.register(Maint)
admin.site.register(Battery)
