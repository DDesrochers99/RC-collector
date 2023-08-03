from django.shortcuts import render
from .models import RemoteControlVehicle
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")


# def rc_index(request):
#     rc = RemoteControlVehicle.objects.all()
#     return render(request, "rc/index.html", {"rc": rc})

def rc_detail(request, rc_id):
    rc_instance = RemoteControlVehicle.objects.get(id=rc_id)
    return render(request, 'rc/details.html', {'rc': rc_instance})


class RemoteControlVehicleList(ListView):
    model = RemoteControlVehicle


class RemoteControlVehicleCreate(CreateView):
    model = RemoteControlVehicle
    fields = "__all__"


class RemoteControlVehicleUpdate(UpdateView):
    model = RemoteControlVehicle
    fields = "__all__"


class RemoteControlVehicleDelete(DeleteView):
    model = RemoteControlVehicle
    success_url = "/rc"