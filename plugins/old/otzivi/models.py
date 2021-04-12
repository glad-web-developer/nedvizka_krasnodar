from cms.models import  CMSPlugin
from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField


class OtziviLvPluginSetting(CMSPlugin):
    class Meta:
        verbose_name = 'Отзывы слайдер'
        verbose_name_plural = 'Отзывы слайдеры'

    def __str__(self):
        return 'Отзывы слайдер'



class OtziviDvPluginSetting(CMSPlugin):
    class Meta:
        verbose_name = 'Отзывы - слайд'
        verbose_name_plural = 'Отзывы - слайды'

    avtor = models.CharField(verbose_name='Автор', blank=True, null=True, max_length=255)
    img = models.ImageField(verbose_name='Превью автора', blank=True, null=True)
    opisanie = models.TextField(verbose_name='Отзыв', blank=True, null=True)
    data = models.DateField(verbose_name='Дата', blank=True, null=True)

    ssilla = models.CharField('Ссылка', null=True, blank=True, max_length=500)
    nazvanie_otzivnika = models.CharField('Название отзывника', null=True, blank=True, max_length=255)

    def __str__(self):
        return f'{self.avtor}'

