#можно создать класс, на основе которого содается табличка в базе данных

from django.db import models

# Create your models here.
from django.db import models



# class AyaYa(models.Model):
#     title = models.CharField(
#         'Название',
#         max_length=250,
#     )
#     img = models.ImageField(
#         'Фото',
#     )
#
# class Kv(models.Model):
#     atag = models.IntegerField(
#         'этаж',
#     )
#     vsatag = models.IntegerField(
#         'всего этажей'
#     )
#     god = models.IntegerField(
#         'год постройки'
#     )
#     plo = models.IntegerField(
#         'Площадь квартиры',
#     )
#     plokyx = models.IntegerField(
#         'Площадь кухни'
#     )
#     kolvo_kov = models.IntegerField(
#         'Колво комнат'
#     )
#     plgl = models.IntegerField(
#         'Площадь жилых комнат'
#     )
#
# class Data(models.Model):
#     FIO = models.CharField(
#         'ФИО',
#         max_length=250
#
#     )
#     gmail = models.CharField(
#         'почта',
#         max_length=150
#     )