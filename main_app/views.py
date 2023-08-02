from django.shortcuts import render
from .models import RemoteControlVehicle

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")


def rc_index(request):
    rc = RemoteControlVehicle.objects.all()
    print(rc)
    return render(request, "rc/index.html", {"rc": rc})

def rc_detail(request, rc_id):
    rc_instance = RemoteControlVehicle.objects.get(id=rc_id)
    return render(request, 'rc/details.html', {'rc': rc_instance})
