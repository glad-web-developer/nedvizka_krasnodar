from cms.models import PlaceholderField, CMSPlugin
from django.db import models
from django.template.defaultfilters import striptags
from django.utils.safestring import mark_safe
from djangocms_text_ckeditor.fields import HTMLField
from easy_thumbnails.files import get_thumbnailer
from filer.fields.image import FilerImageField


# *** дома продажа ***

class DomProdaza(models.Model):
    class Meta:
        verbose_name = 'Дом - продажа'
        verbose_name_plural = 'Дома - продажа'

    pokazivat = models.BooleanField('Показывать/скрыть', default=True, choices=(
        (True, 'Показывать на сайте'),
        (False, 'Не показывать на сайте'),
    ))

    eto_luchoe_prodlozenie = models.IntegerField('Лучшее предложение?', default=1, choices=(
        (1, 'Нет'),
        (2, 'Да. Выводить только на странице лучших предложений'),
        (3, 'Да. Выводить на странице лучших предложений и главной'),
    ))

    nazvanie = models.CharField('Название', max_length=255, null=True, blank=True)
    # nomer = models.CharField('Номер(id объекта)', max_length=50, null=True, blank=True)
    slug = models.SlugField('Ссылка', max_length=255, null=True, blank=True)
    previu = FilerImageField(verbose_name='Превью', null=True, blank=True, on_delete=models.CASCADE)
    price_bazovaia = models.FloatField('Базовая цена руб.', null=True, blank=True,)
    prrice_akzionnaia = models.FloatField('Акционная цена руб', null=True, blank=True,)

    obshaia_ploshad = models.FloatField('Площадь участка и дома (кв. м)', null=True, blank=True)
    naselenii_punkt = models.CharField('Населенный пункт', null=True, blank=True, max_length=255)
    adres = models.CharField('Адрес', null=True, blank=True, max_length=255)
    kordinati_na_karte = models.CharField('Координаты на карте', null=True, blank=True, max_length=255, help_text='Например "44.533249, 33.455248" без кавычек (https://snipp.ru/tools/address-coord)')
    # ploshad_uchastka = models.FloatField('Площадь участка (соток)', null=True, blank=True, max_length=255)
    ploshad_osnovnogo_doma = models.FloatField('Площадь основного дома(кв.м)', null=True, blank=True, max_length=255)

    nalichie_gaza = models.BooleanField('Наличие газа в доме', default=False)
    blizost_so_shkoloi = models.BooleanField('Близость со школой', default=False)
    blizost_s_med = models.BooleanField('Близость с мед учереждением', default=False)
    blizost_s_metro = models.BooleanField('Близость с метро', default=False)
    nalichie_otdelki = models.IntegerField('Наличие отделки', default=1, choices=(
        (1, 'Без отделки'),
        (2, 'Черновая'),
        (3, 'С ремонтом'),
    ))

    opisaanaie = HTMLField('Описание', null=True, blank=True,
                           help_text='Будет выводиться только если выбран шаблонное оформление страницы объекта')



    def get_opisaanaie_kratkoe(self):
        if self.opisaanaie:
            opisanie = striptags(self.opisaanaie)
            return opisanie[0:300] + '...'

    def get_foto_set(self):
        return self.foto_set.select_related('img')

    def get_colvo_img(self):
        return self.foto_set.select_related('img').count()

    def __str__(self):
        try:
            return f'{self.nomer} - {self.nazvanie}'
        except Exception:
            return ''

    def get_url(self):
        if self.slug:
            return self.slug
        return self.id


class FotoDomProdaza(models.Model):
    class Meta:
        verbose_name = 'Фото дома'
        verbose_name_plural = 'Фото дома'
        ordering = ['-index_sortirivki']

    dom = models.ForeignKey(DomProdaza, verbose_name='Дом', on_delete=models.CASCADE, null=True, blank=True,
                            related_name='foto_set')
    img = FilerImageField(verbose_name='Фото', on_delete=models.CASCADE)
    index_sortirivki = models.IntegerField('Индекс сортировки', default=0, help_text='Чем больше тем раньше выведет')

    def __str__(self):
        return f'Фото {self.img.url}'


class VideoDomProdaza(models.Model):
    class Meta:
        verbose_name = 'Видео дома'
        verbose_name_plural = 'Видео дома'
        ordering = ['-index_sortirivki']

    dom = models.ForeignKey(DomProdaza, verbose_name='Дом', on_delete=models.CASCADE, null=True, blank=True,
                            related_name='video_set')
    video = models.TextField('Iframe код видео',
                             help_text='Будет выводиться только если выбран шаблонное оформление страницы объекта')
    index_sortirivki = models.IntegerField('Индекс сортировки', default=0, help_text='Чем больше тем раньше выведет')

    def __str__(self):
        return str(self.id)

class PanoramiDomProdaza(models.Model):
    class Meta:
        verbose_name = 'Панорамы домов'
        verbose_name_plural = 'Панорамы домов'
        ordering = ['-index_sortirivki']

    dom = models.ForeignKey(DomProdaza, verbose_name='Дом', on_delete=models.CASCADE, null=True, blank=True,
                            related_name='panorami_set')
    iframe_code = models.TextField('iframe код',
                                   help_text='Будет выводиться только если выбран шаблонное оформление страницы объекта')
    index_sortirivki = models.IntegerField('Индекс сортировки', default=0, help_text='Чем больше тем раньше выведет')

    def __str__(self):
        return str(self.id)

# -------------


class DomArenda(models.Model):
    class Meta:
        verbose_name = 'Дом - аренда'
        verbose_name_plural = 'Дома - аренда'

    pokazivat = models.BooleanField('Показывать', default=True, choices=(
        (True, 'Показывать на сайте'),
        (False, 'Не показывать на сайте'),
    ))

    eto_luchoe_prodlozenie = models.IntegerField('Лучшее предложение?', default=1, choices=(
        (1, 'Нет'),
        (2, 'Да. Выводить только на странице лучших предложений'),
        (3, 'Да. Выводить на странице лучших предложений и главной'),
    ))

    nazvanie = models.CharField('Название', max_length=255)
    # nomer = models.CharField('Номер(id объекта)', max_length=50, null=True, blank=True)
    slug = models.SlugField('Ссылка', max_length=255, null=True, blank=True)
    previu = FilerImageField(verbose_name='Превью', null=True, blank=True, on_delete=models.CASCADE)
    price_bazovaia = models.FloatField('Базовая цена руб.', null=True, blank=True, )
    prrice_akzionnaia = models.FloatField('Акционная цена руб', null=True, blank=True, )

    obshaia_ploshad = models.FloatField('Плоащдь участка и дома (кв. м)', null=True, blank=True)
    naselenii_punkt = models.CharField('Населенный пункт', null=True, blank=True, max_length=255)
    adres = models.CharField('Адрес', null=True, blank=True, max_length=255)
    kordinati_na_karte = models.CharField('Координаты на карте', null=True, blank=True, max_length=255,
                                          help_text='Например "44.533249, 33.455248" без кавычек (https://snipp.ru/tools/address-coord)')
    # ploshad_uchastka = models.FloatField('Площадь участка (соток)', null=True, blank=True, max_length=255)
    ploshad_osnovnogo_doma = models.FloatField('Площадь основного дома(кв.м)', null=True, blank=True, max_length=255)

    nalichie_gaza = models.BooleanField('Наличие газа в доме', default=False)
    blizost_so_shkoloi = models.BooleanField('Близость со школой', default=False)
    blizost_s_med = models.BooleanField('Близость с мед учереждением', default=False)
    blizost_s_metro = models.BooleanField('Близость с метро', default=False)
    nalichie_otdelki = models.IntegerField('Наличие отделки', default=1, choices=(
        (1, 'Без отделки'),
        (2, 'Черновая'),
        (3, 'С ремонтом'),
    ))

    opisaanaie = HTMLField('Описание', null=True, blank=True,
                           help_text='Будет выводиться только если выбран шаблонное оформление страницы объекта')

    def get_opisaanaie_kratkoe(self):
        if self.opisaanaie:
            opisanie = striptags(self.opisaanaie)
            return opisanie[0:300] + '...'

    def get_foto_set(self):
        return self.foto_set.select_related('img')

    def get_colvo_img(self):
        return self.foto_set.select_related('img').count()

    def __str__(self):
        try:
            return f'{self.nomer} - {self.nazvanie}'
        except Exception:
            return ''

    def get_url(self):
        if self.slug:
            return self.slug
        return self.id


class FotoDomArenda(models.Model):
    class Meta:
        verbose_name = 'Фото дома'
        verbose_name_plural = 'Фото дома'
        ordering = ['-index_sortirivki']

    dom = models.ForeignKey(DomArenda, verbose_name='Дом', on_delete=models.CASCADE, null=True, blank=True,
                            related_name='foto_set')
    img = FilerImageField(verbose_name='Фото', on_delete=models.CASCADE)
    index_sortirivki = models.IntegerField('Индекс сортировки', default=0, help_text='Чем больше тем раньше выведет')

    def __str__(self):
        return f'Фото {self.img.url}'


class VideoDomArendda(models.Model):
    class Meta:
        verbose_name = 'Видео дома'
        verbose_name_plural = 'Видео дома'
        ordering = ['-index_sortirivki']

    dom = models.ForeignKey(DomArenda, verbose_name='Дом', on_delete=models.CASCADE, null=True, blank=True,
                            related_name='video_set')
    video = models.TextField('Iframe код видео',
                             help_text='Будет выводиться только если выбран шаблонное оформление страницы объекта')
    index_sortirivki = models.IntegerField('Индекс сортировки', default=0, help_text='Чем больше тем раньше выведет')

    def __str__(self):
        return str(self.id)


class PanoramiArenda(models.Model):
    class Meta:
        verbose_name = 'Панорамы домов'
        verbose_name_plural = 'Панорамы домов'
        ordering = ['-index_sortirivki']

    dom = models.ForeignKey(DomArenda, verbose_name='Дом', on_delete=models.CASCADE, null=True, blank=True,
                            related_name='panorami_set')
    iframe_code = models.TextField('iframe код',
                                   help_text='Будет выводиться только если выбран шаблонное оформление страницы объекта')
    index_sortirivki = models.IntegerField('Индекс сортировки', default=0, help_text='Чем больше тем раньше выведет')

    def __str__(self):
        return str(self.id)