from cms.models import PlaceholderField, CMSPlugin
from django.db import models
from django.template.defaultfilters import striptags
from django.utils.safestring import mark_safe
from djangocms_text_ckeditor.fields import HTMLField
from easy_thumbnails.files import get_thumbnailer
from filer.fields.image import FilerImageField

from apps.nedvizka.CONST import CHOICES_POKAZIVAT, CHOICES_ETO_LUCHSHOE_PREDLOZENIE, CHOICES_NALICHIE_OTDELKI, \
    KOLVO_SIMVOLOV_OBREZKI, CHOICES_DA_NET
from apps.nedvizka.models import Nedvizka


class KvartiraVtorichkaProdaza(Nedvizka):
    class Meta:
        verbose_name = 'Квартира вторичка - продажа'
        verbose_name_plural = '-Квартира вторичка - продажа'
        ordering = ['-id']

    nalichie_gaza = models.BooleanField('Наличие газа', default=False, choices=CHOICES_DA_NET)
    blizost_so_shkoloi = models.BooleanField('Близость со школой/садиком/садиком', default=False,
                                             choices=CHOICES_DA_NET)
    blizost_s_med = models.BooleanField('Близость с мед учереждением', default=False, choices=CHOICES_DA_NET)
    blizost_s_metro = models.BooleanField('Близость с метро', default=False, choices=CHOICES_DA_NET)
    nalichie_otdelki = models.IntegerField('Наличие отделки', default=1, choices=CHOICES_NALICHIE_OTDELKI)
    ostanovki = models.CharField('Остановки', blank=True, null=True, max_length=255)


class FotoKvartiraVtorichkaProdaza(models.Model):
    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
        ordering = ['-index_sortirivki']

    nedvizka = models.ForeignKey(KvartiraVtorichkaProdaza, verbose_name='Недвижка', on_delete=models.CASCADE, null=True, blank=True,
                            related_name='foto_set')
    img = FilerImageField(verbose_name='Фото', on_delete=models.CASCADE)
    index_sortirivki = models.IntegerField('Индекс сортировки', default=0, help_text='Чем больше тем раньше выведет')

    def __str__(self):
        return f'Фото {self.img.url}'

