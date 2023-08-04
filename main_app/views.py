from django.shortcuts import render, redirect
from .models import RemoteControlVehicle, Battery
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .forms import MaintForm


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")



def add_maint(request, rc_id):
    form = MaintForm(request.POST)
    if form.is_valid():
        new_maint = form.save(commit=False)
        new_maint.rc_id = rc_id
        new_maint.save()
    return redirect("detail", rc_id=rc_id)


def assoc_battery(request, rc_id, battery_id):
  RemoteControlVehicle.objects.get(id=rc_id).batterys.add(battery_id)
  return redirect('detail', rc_id=rc_id)

def unassoc_battery(request, rc_id, battery_id):
  RemoteControlVehicle.objects.get(id=rc_id).batterys.remove(battery_id)
  return redirect('detail', rc_id=rc_id)

class batteryCreate(CreateView):
  model = Battery
  fields = '__all__'

class batteryDetail(DetailView):
  model = Battery

class batteryList(ListView):
  model = Battery


class batteryUpdate(UpdateView):
  model = Battery
  fields = '__all__'

class batteryDelete(DeleteView):
  model = Battery
  success_url = '/battery'


def rc_detail(request, rc_id):
    rc_instance = RemoteControlVehicle.objects.get(id=rc_id)
    id_list = rc_instance.batterys.all().values_list('id')

    batterys_rc_doesnt_have = Battery.objects.exclude(id__in=id_list)
    maint_form = MaintForm()
    return render(
        request,
        "rc/details.html",
        {
            "rc": rc_instance,
            "maint_form": maint_form,
            'batterys': batterys_rc_doesnt_have
        },
    )


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
