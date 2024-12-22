from django.db import models

# Create your models here.
class Cars(models.Model):
    nameAuto = models.CharField(max_length=255, blank=False, null=False)
    descriptionAuto = models.TextField(blank=False, null=False)
    # priceAuto = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    imageAuto = models.ImageField(verbose_name="Картинка атомобиля", null=True, upload_to='cars/')


def __str__(self):
    return f'{self.nameAuto}'


class Meta:
    verbose_name = 'Автомобиль'
    verbose_name_plural = 'Автомобили'
