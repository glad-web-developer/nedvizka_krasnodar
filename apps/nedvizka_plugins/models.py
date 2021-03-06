from cms.models import PlaceholderField, CMSPlugin
from django.db import models
from django.utils.safestring import mark_safe
from djangocms_text_ckeditor.fields import HTMLField
from easy_thumbnails.files import get_thumbnailer
from filer.fields.image import FilerImageField

TIP_NEDVIZKI = (
    ('dom_prodaza', 'Дом-продажа'),
    # ('dom_arenda', 'Дом-аренда'),

    ('kvartira_pervicka_prodaza', 'Квартира первичка - продажа'),
    # ('kvartira_pervicka_arenda', 'Квартира первичка - аренда'),

    ('kvartira_vtoricka_prodaza', 'Квартира вторичка - продажа'),
    # ('kvartira_vtoricka_arenda', 'Квартира вторичка - аренда'),

    ('kvartira_vtoricka_prodaza', 'Квартира вторичка - продажа'),
    # ('kvartira_vtoricka_arenda', 'Квартира вторичка - аренда'),

    ('uchactki_prodaza', 'Участки - продажа'),
    # ('uchactki_arenda', 'Участки - аренда'),

    ('nezilie_prodaza', 'Нежилые - продажа'),
    # ('nezilie_arenda', 'Нежилые - аренда'),

    ('komerchiskie_prodaza', 'Комерчиские - продажа'),
    # ('komerchiskie_arenda', 'Комерчиские - аренда'),
    ('maloetaznoe_stroitelstvo', 'Малоэтажное строительство'),
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


class NedvizkaFiltriPoiskaPluginPluginSetting(CMSPlugin):
    class Meta:
        verbose_name = 'Недвижка. Фильтры/поиск'
        verbose_name_plural = 'Недвижка. Фильтры/поиск'

    tip_nedvizki = models.CharField('Тип недвижки', max_length=255, choices=TIP_NEDVIZKI)

