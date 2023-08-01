from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")


def rc_index(request):
    return render(request, "rc/index.html")

def index_view(request):
    vehicles = RemoteControlVehicle.objects.all()
    return render(request, 'rc/index.html', {'remote_control_vehicles': vehicles})