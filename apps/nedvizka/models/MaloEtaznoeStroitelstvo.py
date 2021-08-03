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


class MaterialMaoetaznoiPostroiki(models.Model):
    class Meta:
        verbose_name = 'Материал постройки малоэтажной стройки'
        verbose_name_plural = 'Материалы постройки малоэтажной стройки'

    nazvanie = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.nazvanie


class TipMaloetaznoiPostroiki(models.Model):
    class Meta:
        verbose_name = 'Материал постройки малоэтажной стройки'
        verbose_name_plural = 'Материалы постройки малоэтажной стройки'

    nazvanie = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.nazvanie


class MaloEtaznoeStroitelstvoProdaza(models.Model):
    class Meta:
        verbose_name = 'Малоэтажное строительство - продажа'
        verbose_name_plural = 'Малоэтажное строительство - продажа'

    pokazivat = models.BooleanField('Показывать/скрыть', default=True, choices=CHOICES_POKAZIVAT)
    tip_maloetaznoi_postroiki = models.ForeignKey(TipMaloetaznoiPostroiki, verbose_name='Тип', null=True, blank=True,
                                                  on_delete=models.SET_NULL)

    nazvanie = models.CharField('Название', max_length=255, null=True, blank=True)
    previu = FilerImageField(verbose_name='Превью', null=True, blank=True, on_delete=models.CASCADE)
    price_bazovaia = models.FloatField('Базовая цена руб.', default=0)

    material_postroiki = models.ForeignKey(MaterialMaoetaznoiPostroiki, blank=True, null=True, verbose_name='Материал',
                                           on_delete=models.SET_NULL)

    obshaia_ploshad = models.FloatField('Общая площадь', null=True, blank=True, max_length=255)

    kolvo_etazei = models.CharField('Количество этажей', blank=True, null=True, max_length=10)
    kolvo_komnat = models.IntegerField('Количество комнат', blank=True, null=True)

    opisaanaie = HTMLField('Описание', null=True, blank=True,
                           help_text='Будет выводиться только если выбран шаблонное оформление страницы объекта')

    prrice_akzionnaia = models.FloatField('Акционная цена руб', default=0)
    price_itogovaia = models.FloatField('Цена для поиска', default=0)
    akzia = models.BooleanField('Акция/спец цена', default=False, editable=False)

    def get_pervonochalnii_vznos(self):
        if self.price_itogovaia:
            return int(self.price_itogovaia / 10)

    def get_nazvanie(self):
        if self.nazvanie:
            return self.nazvanie
        return f'Дом №{self.id}'

    def get_opisaanaie_kratkoe(self):
        if self.opisaanaie:
            opisanie = striptags(self.opisaanaie)
            return opisanie[0:KOLVO_SIMVOLOV_OBREZKI] + '...'

    def get_foto_set(self):
        return self.foto_set.select_related('img')

    def get_colvo_img(self):
        return self.foto_set.select_related('img').count()

    def __str__(self):
        try:
            return f'{self.nazvanie}'
        except Exception:
            return ''

    def get_url(self):
        return self.id

    def save(self, *args, **kwargs):
        if self.prrice_akzionnaia > 0:
            self.akzia = True
            self.price_itogovaia = self.prrice_akzionnaia
        else:
            self.akzia = False
            self.price_itogovaia = self.price_bazovaia
        super().save(*args, **kwargs)


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
