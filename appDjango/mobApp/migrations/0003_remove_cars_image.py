# Generated by Django 5.1.4 on 2024-12-19 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobApp', '0002_alter_cars_priceauto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='image',
        ),
    ]
