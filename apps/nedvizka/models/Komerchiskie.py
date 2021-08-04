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


class TipKomerch(models.Model):
    class Meta:
        verbose_name = 'Комерчиский - тип'
        verbose_name_plural = 'Комерчиский - тип'
        ordering = ['-id']

    nazvanie = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.nazvanie

class KomerchiskieProdaza(Nedvizka):
    class Meta:
        verbose_name = 'Комерчиские - продажа'
        verbose_name_plural = '-Комерчиские - продажа'
        ordering = ['-id']

    tip_komerch = models.ForeignKey(TipKomerch, verbose_name='Тип', null=True, blank=True, on_delete=models.PROTECT)


class FotoKomerchiskieProdaza(models.Model):
    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
        ordering = ['-index_sortirivki']

    nedvizka = models.ForeignKey(KomerchiskieProdaza, verbose_name='Недвижка', on_delete=models.CASCADE, null=True, blank=True,
                            related_name='foto_set')
    img = FilerImageField(verbose_name='Фото', on_delete=models.CASCADE)
    index_sortirivki = models.IntegerField('Индекс сортировки', default=0, help_text='Чем больше тем раньше выведет')

    def __str__(self):
        return f'Фото {self.img.url}'

