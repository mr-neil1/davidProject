# dashboard/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/sensor/', views.fetch_flask_data, name='sensor_data'),
]

