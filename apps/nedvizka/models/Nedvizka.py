from django.db import models
from django.template.defaultfilters import striptags
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField

from apps.nedvizka.CONST import CHOICES_POKAZIVAT, KOLVO_SIMVOLOV_OBREZKI


class Nedvizka(models.Model):
    class Meta:
        abstract = True

    pokazivat = models.BooleanField('Показывать/скрыть', default=True, choices=CHOICES_POKAZIVAT)
    nazvanie = models.CharField('Название', max_length=255, null=True, blank=True)
    slug = models.SlugField('Ссылка', max_length=255, null=True, blank=True, editable=False)
    previu = FilerImageField(verbose_name='Превью', null=True, blank=True, on_delete=models.CASCADE)
    price_bazovaia = models.FloatField('Базовая цена руб.', default=0)

    prrice_akzionnaia = models.FloatField('Акционная цена руб', default=0, null=True, blank=True)
    price_itogovaia = models.FloatField('Цена для поиска', default=0, editable=False)
    akzia = models.BooleanField('Акция/спец цена', default=False,  editable=False)

    obshaia_ploshad = models.FloatField('Площадь (кв. м)', null=True, blank=True)


    naselenii_punkt = models.CharField('Населенный пункт', null=True, blank=True, max_length=255)
    adres = models.CharField('Адрес', null=True, blank=True, max_length=255)

    kordinati_na_karte = models.CharField('Координаты на карте', null=True, blank=True, editable=False, max_length=255,
                                          help_text='Например "44.533249, 33.455248" без кавычек (https://snipp.ru/tools/address-coord)')


    opisaanaie = HTMLField('Описание', null=True, blank=True,
                           help_text='Будет выводиться только если выбран шаблонное оформление страницы объекта')

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
        if self.slug:
            return self.slug
        return self.id

    def save(self, *args, **kwargs):
        if self.prrice_akzionnaia > 0:
            self.akzia = True
            self.price_itogovaia = self.prrice_akzionnaia
        else:
            self.akzia = False
            self.price_itogovaia = self.price_bazovaia
        super().save(*args, **kwargs)
