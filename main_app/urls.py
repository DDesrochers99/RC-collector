from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name='about'),
    path('rc/', views.RemoteControlVehicleList.as_view(), name='rc_index'),
    path('rc/create/', views.RemoteControlVehicleCreate.as_view(), name='rc_create'),
    path('rc/<int:rc_id>/', views.rc_detail, name='detail'),
    path('rc/<int:rc_id>/add_maint/', views.add_maint, name='add_maint'),
    path('rc/<int:pk>/update/', views.RemoteControlVehicleUpdate.as_view(), name='rc_update'),
    path('rc/<int:pk>/delete/', views.RemoteControlVehicleDelete.as_view(), name='rc_delete'),
    path('battery/create/', views.batteryCreate.as_view(), name='battery_create'),
    path('battery/', views.batteryList.as_view(), name='batterys_index'),
    path('battery/<int:pk>/', views.batteryDetail.as_view(), name='batterys_detail'),
    path('battery/<int:pk>/update/', views.batteryUpdate.as_view(), name='batterys_update'),
    path('battery/<int:pk>/delete/', views.batteryDelete.as_view(), name='batterys_delete'),
    path('rc/<int:rc_id>/assoc_battery/<int:battery_id>/', views.assoc_battery, name='assoc_battery'),
    path('rc/<int:rc_id>/unassoc_battery/<int:battery_id>/', views.unassoc_battery, name='unassoc_battery'),
]