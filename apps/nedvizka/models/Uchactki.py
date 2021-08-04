from django.db import models
from django.db import models
from filer.fields.image import FilerImageField

from apps.nedvizka.CONST import CHOICES_DA_NET
from apps.nedvizka.models import Nedvizka


class UchactkiProdaza(Nedvizka):
    class Meta:
        verbose_name = 'Участки - продажа'
        verbose_name_plural = '-Участки - продажа'
        ordering = ['-id']

    vodoprovod = models.BooleanField('Водопровод',  null=True, blank=True, choices=CHOICES_DA_NET)
    electrichestvo = models.BooleanField('Электричество',  null=True, blank=True, choices=CHOICES_DA_NET)
    ostanovki = models.CharField('Остановки', blank=True, null=True, max_length=255)


class FotoUchactkiProdaza(models.Model):
    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
        ordering = ['-index_sortirivki']

    nedvizka = models.ForeignKey(UchactkiProdaza, verbose_name='Недвижка', on_delete=models.CASCADE, null=True, blank=True,
                            related_name='foto_set')
    img = FilerImageField(verbose_name='Фото', on_delete=models.CASCADE)
    index_sortirivki = models.IntegerField('Индекс сортировки', default=0, help_text='Чем больше тем раньше выведет')

    def __str__(self):
        return f'Фото {self.img.url}'