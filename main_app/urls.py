from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name='about'),
    path('rc/', views.rc_index, name='index'),
    path('rc/<int:rc_id>/', views.rc_detail, name='detail'),
]