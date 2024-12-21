from rest_framework import serializers
from .models import Cars

class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ['id', 'nameAuto', 'descriptionAuto', 'imageAuto']

    # def validate_nameAuto(self, value):
    #     if not value.strip():
    #         raise serializers.ValidationError("Название автомобиля не может быть пустым.")
    #     return value
    #
    # def validate(self, data):
    #     if not data.get('descriptionAuto'):
    #         raise serializers.ValidationError("Описание обязательно.")
    #     return data
