from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Cars
from .serializes import AutoSerializer

class CarsSerializerGet(APIView):
    def get(self, request):
        cars = Cars.objects.all()
        serializer = AutoSerializer(cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
# Create your views here.




# def add_auto(request):
#     if request.method == 'POST':
#         serializer = AutoSerializer(data=request.data)
#         if serializer.is_valid():
#             # логика для сохранения данных
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

