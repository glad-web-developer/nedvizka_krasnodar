from cms.models import PlaceholderField, CMSPlugin
from django.db import models
from django.template.defaultfilters import striptags
from django.utils.safestring import mark_safe
from djangocms_text_ckeditor.fields import HTMLField
from easy_thumbnails.files import get_thumbnailer
from filer.fields.image import FilerImageField

from apps.nedvizka.CONST import CHOICES_POKAZIVAT, CHOICES_ETO_LUCHSHOE_PREDLOZENIE, CHOICES_NALICHIE_OTDELKI, \
    KOLVO_SIMVOLOV_OBREZKI, CHOICES_DA_NET


class NezelieProdaza(models.Model):
    class Meta:
        verbose_name = 'Нежилые - продажа'
        verbose_name_plural = 'Нежилые - продажа'

    pokazivat = models.BooleanField('Показывать/скрыть', default=True, choices=CHOICES_POKAZIVAT)

    eto_luchoe_prodlozenie = models.IntegerField('Лучшее предложение?', default=1,
                                                 choices=CHOICES_ETO_LUCHSHOE_PREDLOZENIE)

    nazvanie = models.CharField('Название', max_length=255, null=True, blank=True)
    slug = models.SlugField('Ссылка', max_length=255, null=True, blank=True)
    previu = FilerImageField(verbose_name='Превью', null=True, blank=True, on_delete=models.CASCADE)
    price_bazovaia = models.FloatField('Базовая цена руб.', default=0)
    prrice_akzionnaia = models.FloatField('Акционная цена руб', default=0)

    price_itogovaia = models.FloatField('Цена для поиска', default=0)
    akzia = models.BooleanField('Акция/спец цена', default=False)

    obshaia_ploshad = models.FloatField('Площадь участка и дома (кв. м)', null=True, blank=True)
    naselenii_punkt = models.CharField('Населенный пункт', null=True, blank=True, max_length=255)
    adres = models.CharField('Адрес', null=True, blank=True, max_length=255)
    kordinati_na_karte = models.CharField('Координаты на карте', null=True, blank=True, max_length=255,
                                          help_text='Например "44.533249, 33.455248" без кавычек (https://snipp.ru/tools/address-coord)')
    # ploshad_osnovnogo_doma = models.FloatField('Площадь основного дома(кв.м)', null=True, blank=True, max_length=255)

    nalichie_gaza = models.BooleanField('Наличие газа в доме', default=False, choices=CHOICES_DA_NET)
    blizost_so_shkoloi = models.BooleanField('Близость со школой', default=False, choices=CHOICES_DA_NET)
    blizost_s_med = models.BooleanField('Близость с мед учереждением', default=False, choices=CHOICES_DA_NET)
    blizost_s_metro = models.BooleanField('Близость с метро', default=False, choices=CHOICES_DA_NET)
    nalichie_otdelki = models.IntegerField('Наличие отделки', default=1, choices=CHOICES_NALICHIE_OTDELKI)

    opisaanaie = HTMLField('Описание', null=True, blank=True,
                           help_text='Будет выводиться только если выбран шаблонное оформление страницы объекта')

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


class FotoNezelieProdaza(models.Model):
    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
        ordering = ['-index_sortirivki']

    nedvizka = models.ForeignKey(NezelieProdaza, verbose_name='Недвижка', on_delete=models.CASCADE, null=True, blank=True,
                            related_name='foto_set')
    img = FilerImageField(verbose_name='Фото', on_delete=models.CASCADE)
    index_sortirivki = models.IntegerField('Индекс сортировки', default=0, help_text='Чем больше тем раньше выведет')

    def __str__(self):
        return f'Фото {self.img.url}'


class VideoNezelieProdaza(models.Model):
    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
        ordering = ['-index_sortirivki']

    nedvizka = models.ForeignKey(NezelieProdaza, verbose_name='Недвижка', on_delete=models.CASCADE, null=True, blank=True,
                            related_name='video_set')
    video = models.TextField('Iframe код видео',
                             help_text='Будет выводиться только если выбран шаблонное оформление страницы объекта')
    index_sortirivki = models.IntegerField('Индекс сортировки', default=0, help_text='Чем больше тем раньше выведет')

    def __str__(self):
        return str(self.id)


class PanoramiNezelieProdaza(models.Model):
    class Meta:
        verbose_name = 'Панорамы'
        verbose_name_plural = 'Панорамы'
        ordering = ['-index_sortirivki']

    nedvizka = models.ForeignKey(NezelieProdaza, verbose_name='Недвижка', on_delete=models.CASCADE, null=True, blank=True,
                            related_name='panorami_set')
    iframe_code = models.TextField('iframe код',
                                   help_text='Будет выводиться только если выбран шаблонное оформление страницы объекта')
    index_sortirivki = models.IntegerField('Индекс сортировки', default=0, help_text='Чем больше тем раньше выведет')

    def __str__(self):
        return str(self.id)


# -------------


class NezelieArenda(models.Model):
    class Meta:
        verbose_name = 'Нежилые - аренда'
        verbose_name_plural = 'Нежилые - аренда'

    pokazivat = models.BooleanField('Показывать', default=True, choices=CHOICES_POKAZIVAT)

    eto_luchoe_prodlozenie = models.IntegerField('Лучшее предложение?', default=1,
                                                 choices=CHOICES_ETO_LUCHSHOE_PREDLOZENIE)

    nazvanie = models.CharField('Название', max_length=255)
    slug = models.SlugField('Ссылка', max_length=255, null=True, blank=True)
    previu = FilerImageField(verbose_name='Превью', null=True, blank=True, on_delete=models.CASCADE)
    price_bazovaia = models.FloatField('Базовая цена руб.', default=0)
    prrice_akzionnaia = models.FloatField('Акционная цена руб', default=0)

    price_itogovaia = models.FloatField('Цена для поиска', default=0)
    akzia = models.BooleanField('Акция/спец цена', default=False)

    obshaia_ploshad = models.FloatField('Плоащдь участка и дома (кв. м)', null=True, blank=True)
    naselenii_punkt = models.CharField('Населенный пункт', null=True, blank=True, max_length=255)
    adres = models.CharField('Адрес', null=True, blank=True, max_length=255)
    kordinati_na_karte = models.CharField('Координаты на карте', null=True, blank=True, max_length=255,
                                          help_text='Например "44.533249, 33.455248" без кавычек (https://snipp.ru/tools/address-coord)')
    # ploshad_uchastka = models.FloatField('Площадь участка (соток)', null=True, blank=True, max_length=255)
    # ploshad_osnovnogo_doma = models.FloatField('Площадь основного дома(кв.м)', null=True, blank=True, max_length=255)

    nalichie_gaza = models.BooleanField('Наличие газа в доме', default=False, choices=CHOICES_DA_NET)
    blizost_so_shkoloi = models.BooleanField('Близость со школой', default=False, choices=CHOICES_DA_NET)
    blizost_s_med = models.BooleanField('Близость с мед учереждением', default=False, choices=CHOICES_DA_NET)
    blizost_s_metro = models.BooleanField('Близость с метро', default=False, choices=CHOICES_DA_NET)
    nalichie_otdelki = models.IntegerField('Наличие отделки', default=1, choices=CHOICES_NALICHIE_OTDELKI)

    opisaanaie = HTMLField('Описание', null=True, blank=True,
                           help_text='Будет выводиться только если выбран шаблонное оформление страницы объекта')

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


class FotoNezelieArenda(models.Model):
    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
        ordering = ['-index_sortirivki']

    nedvizka = models.ForeignKey(NezelieArenda, verbose_name='Недвижка', on_delete=models.CASCADE, null=True, blank=True,
                            related_name='foto_set')
    img = FilerImageField(verbose_name='Фото', on_delete=models.CASCADE)
    index_sortirivki = models.IntegerField('Индекс сортировки', default=0, help_text='Чем больше тем раньше выведет')

    def __str__(self):
        return f'Фото {self.img.url}'


class VideoNezelieArenda(models.Model):
    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
        ordering = ['-index_sortirivki']

    nedvizka = models.ForeignKey(NezelieArenda, verbose_name='Недвижка', on_delete=models.CASCADE, null=True, blank=True,
                            related_name='video_set')
    video = models.TextField('Iframe код видео',
                             help_text='Будет выводиться только если выбран шаблонное оформление страницы объекта')
    index_sortirivki = models.IntegerField('Индекс сортировки', default=0, help_text='Чем больше тем раньше выведет')

    def __str__(self):
        return str(self.id)


class PanoramiNezelieArenda(models.Model):
    class Meta:
        verbose_name = 'Панорамы'
        verbose_name_plural = 'Панорамы'
        ordering = ['-index_sortirivki']

    nedvizka = models.ForeignKey(NezelieArenda, verbose_name='Недвижка', on_delete=models.CASCADE, null=True, blank=True,
                            related_name='panorami_set')
    iframe_code = models.TextField('iframe код',
                                   help_text='Будет выводиться только если выбран шаблонное оформление страницы объекта')
    index_sortirivki = models.IntegerField('Индекс сортировки', default=0, help_text='Чем больше тем раньше выведет')

    def __str__(self):
        return str(self.id)
