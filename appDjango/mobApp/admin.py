from django.contrib import admin
from .models import Cars
from django.utils.safestring import mark_safe


@admin.register(Cars)
class Cars(admin.ModelAdmin):
    list_display = ('id', 'nameAuto', 'descriptionAuto',  'image')
    list_filter = ('id', 'nameAuto', 'descriptionAuto')
    search_fields = ('id', 'nameAuto', 'descriptionAuto')

    readonly_fields = ["image"]

    def image(self, obj):
        return mark_safe(f'<img width="180px" src="{obj.imageAuto.url}">')

    image.short_description = "Картинка автомобиля"
# Register your models here.