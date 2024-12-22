from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Cars
from .serializes import AutoSerializer
from django.http import HttpResponse
from .forms import CarsForm

class CarsSerializerGet(APIView):
    def get(self, request):
        cars = Cars.objects.all()
        serializer = AutoSerializer(cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
# Create your views here.


def updatecar(request):
    if request.method == "POST":
        form = CarsForm(request.POST, request.FILES)
        print(form.is_valid())
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CarsForm()
    context = {
        'form': form
    }
    return render(request, "addcars.html", context)


# def add_auto(request):
#     if request.method == 'POST':
#         serializer = AutoSerializer(data=request.data)
#         if serializer.is_valid():
#             # логика для сохранения данных
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

