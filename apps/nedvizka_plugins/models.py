from cms.models import PlaceholderField, CMSPlugin
from django.db import models
from django.utils.safestring import mark_safe
from djangocms_text_ckeditor.fields import HTMLField
from easy_thumbnails.files import get_thumbnailer
from filer.fields.image import FilerImageField

TIP_NEDVIZKI = (
    ('dom_prodaza', 'Дом-продажа'),
    ('dom_arenda', 'Дом-аренда'),
)

# *** ПЛАГИНЫ ***

class NedvizkaSpisokObiectovPluginPluginSetting(CMSPlugin):
    class Meta:
        verbose_name = 'Недвижка. Список объектов'
        verbose_name_plural = 'Недвижка. Список объектов'

    def __str__(self):
        return 'Недвижка. Список объектов'

    tip_nedvizki = models.CharField('Тип недвижки', max_length=255, choices=TIP_NEDVIZKI)

    obiectov_na_stranize = models.IntegerField('Выводить по ', default=10)

    css_class = models.CharField('CSS класс', null=True, blank=True, max_length=255)
    css_style = models.CharField('CSS стиль', null=True, blank=True, max_length=1000)

    def get_short_description(self):
        tip_nedvizki = self.tip_nedvizki or '-'
        obiectov_na_stranize = self.obiectov_na_stranize or '-'
        return f'{tip_nedvizki} (по {obiectov_na_stranize} шт.)'


class NedvizkaIzbranoePluginSetting(CMSPlugin):
    class Meta:
        verbose_name = 'Недвижка. Избранное'
        verbose_name_plural = 'Недвижка. Избранное'

    def __str__(self):
        return 'Недвижка. Избранное'

    css_class = models.CharField('CSS класс', null=True, blank=True, max_length=255)
    css_style = models.CharField('CSS стиль', null=True, blank=True, max_length=1000)


class NedvizkaPanelUpravleniaPluginSetting(CMSPlugin):
    class Meta:
        verbose_name = 'Недвижка. Избранное'
        verbose_name_plural = 'Недвижка. Избранное'

    def __str__(self):
        return 'Недвижка. Избранное'

    pokazat_kartu = models.BooleanField('Показывать карту', default=True)
    pokazat_sortirovku = models.BooleanField('Показывать сортировку', default=True)
    css_class = models.CharField('CSS класс', null=True, blank=True, max_length=255)
    css_style = models.CharField('CSS стиль', null=True, blank=True, max_length=1000)


class NedvizkaFiltriPoiskaPluginPluginSetting(CMSPlugin):
    class Meta:
        verbose_name = 'Недвижка. Фильтры/поиск'
        verbose_name_plural = 'Недвижка. Фильтры/поиск'

    tip_nedvizki = models.CharField('Тип недвижки', max_length=255, choices=TIP_NEDVIZKI)

