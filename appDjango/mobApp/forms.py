from django.forms import ModelForm
from .models import Cars


class CarsForm(ModelForm):
    class Meta:
        model = Cars
        fields = ['nameAuto', 'descriptionAuto', 'imageAuto']
