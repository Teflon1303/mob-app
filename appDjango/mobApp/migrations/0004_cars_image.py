# Generated by Django 5.1.4 on 2024-12-19 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobApp', '0003_remove_cars_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='image',
            field=models.ImageField(null=True, upload_to='static/img/cars/', verbose_name='Картинка атомобиля'),
        ),
    ]