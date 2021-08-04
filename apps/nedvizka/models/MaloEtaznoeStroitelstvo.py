from cms.models import PlaceholderField, CMSPlugin
from django.db import models
from django.template.defaultfilters import striptags
from django.utils.safestring import mark_safe
from djangocms_text_ckeditor.fields import HTMLField
from easy_thumbnails.files import get_thumbnailer
from filer.fields.image import FilerImageField

# *** дома продажа ***
from apps.nedvizka.CONST import CHOICES_POKAZIVAT, CHOICES_ETO_LUCHSHOE_PREDLOZENIE, CHOICES_NALICHIE_OTDELKI, \
    KOLVO_SIMVOLOV_OBREZKI, CHOICES_DA_NET
from apps.nedvizka.models import Nedvizka


class MaterialMaoetaznoiPostroiki(models.Model):
    class Meta:
        verbose_name = 'Материал постройки малоэтажной стройки'
        verbose_name_plural = 'Материалы постройки малоэтажной стройки'

    nazvanie = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.nazvanie


class TipMaloetaznoiPostroiki(models.Model):
    class Meta:
        verbose_name = 'Тип постройки малоэтажной стройки'
        verbose_name_plural = 'Тип постройки малоэтажной стройки'

    nazvanie = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.nazvanie


class MaloEtaznoeStroitelstvoProdaza(Nedvizka):
    class Meta:
        verbose_name = 'Малоэтажное строительство - продажа'
        verbose_name_plural = '-Малоэтажное строительство - продажа'
        ordering = ['-id']
    tip_maloetaznoi_postroiki = models.ForeignKey(TipMaloetaznoiPostroiki, verbose_name='Тип', null=True, blank=True,
                                                  on_delete=models.SET_NULL)


    material_postroiki = models.ForeignKey(MaterialMaoetaznoiPostroiki, blank=True, null=True, verbose_name='Материал',
                                           on_delete=models.SET_NULL)


    kolvo_etazei = models.CharField('Количество этажей', blank=True, null=True, max_length=10)
    kolvo_komnat = models.IntegerField('Количество комнат', blank=True, null=True)



class FotoMaloEtaznoeStroitelstvoProdaza(models.Model):
    class Meta:
        verbose_name = 'Фото дома'
        verbose_name_plural = 'Фото дома'
        ordering = ['-index_sortirivki']

    dom = models.ForeignKey(MaloEtaznoeStroitelstvoProdaza, verbose_name='Дом', on_delete=models.CASCADE, null=True,
                            blank=True,
                            related_name='foto_set')
    img = FilerImageField(verbose_name='Фото', on_delete=models.CASCADE)
    index_sortirivki = models.IntegerField('Индекс сортировки', default=0, help_text='Чем больше тем раньше выведет')

    def __str__(self):
        return f'Фото {self.img.url}'
