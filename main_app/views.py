from django.shortcuts import render

remote_control_vehicles = [
    {'brand': 'Traxxas', 'model': 'Slash 4x4', 'description': 'High-performance off-road truck', 'price': 399.99},
    {'brand': 'Redcat Racing', 'model': 'Everest 10', 'description': 'Rock crawler with excellent traction', 'price': 299.99},
    {'brand': 'HPI Racing', 'model': 'Savage XS Flux', 'description': 'Compact and powerful monster truck', 'price': 349.99},
]

# Create your views here.
def home(request):
    return render(request, "home.html")

def index(request):
    return render(request, "index.html")