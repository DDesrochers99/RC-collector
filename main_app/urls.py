from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name='about'),
    # path('rc/', views.rc_index, name='index'),
    path('rc/<int:rc_id>/', views.rc_detail, name='detail'),
    path('rc/', views.RemoteControlVehicleList.as_view(), name='rc_index'),
    path('rc/<int:pk>/update/', views.RemoteControlVehicleUpdate.as_view(), name='rc_update'),
    path('rc/<int:pk>/delete/', views.RemoteControlVehicleDelete.as_view(), name='rc_delete'),
    path('rc/create/', views.RemoteControlVehicleCreate.as_view(), name='rc_create'),
    
]