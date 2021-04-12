from cms.models import  CMSPlugin
from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField


class PriceListLvPluginSetting(CMSPlugin):
    class Meta:
        verbose_name = 'Прайс слайдер'
        verbose_name_plural = 'Прайс слайдер'

    def __str__(self):
        return 'Прайс'



class PriceListDvPluginSetting(CMSPlugin):
    class Meta:
        verbose_name = 'Прайс - слайд'
        verbose_name_plural = 'Прайс - слайд'

    zagolovok = models.TextField(verbose_name='Заголовок', blank=True, null=True)
    img = models.ImageField(verbose_name='Изображение', blank=True, null=True)
    opisanie = HTMLField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f'{self.zagolovok}'

