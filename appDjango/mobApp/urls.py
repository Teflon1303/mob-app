from django.urls import path, include

from . import views
from .serializes import AutoSerializer
from .views import CarsSerializerGet, CarCreate

urlpatterns = [
    # path('', index, name='index'),
    path('api/get/cars/', CarsSerializerGet.as_view(), name='Cars'),
    path('api/post/cars/', CarCreate.as_view(), name='Cars'),
    # path('cars/create/', add_auto.as_view(), name='cars-create'),
]