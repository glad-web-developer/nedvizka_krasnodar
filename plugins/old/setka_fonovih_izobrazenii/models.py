from cms.models import  CMSPlugin
from django.db import models
from filer.fields.image import FilerImageField


class SetkaFonovihIzobrazeniiLvSetting(CMSPlugin):
    class Meta:
        verbose_name = 'Сетка фоновых изображений LV'
        verbose_name_plural = 'Сетка фоновых изображений LV'

    css_class = models.CharField('Класс', max_length=255, blank=True, null=True)
    css_style = models.TextField('Стиль', blank=True, null=True)

    def __str__(self):
        return 'Сетка фоновых изображений LV'


class SetkaFonovihIzobrazeniiDvSetting(CMSPlugin):
    class Meta:
        verbose_name = 'Сетка фоновых изображений DV'
        verbose_name_plural = 'Сетка фоновых изображений DV'

    zagolovok = models.TextField('Заголовок', max_length=255, default='Заголовок')
    img = FilerImageField(verbose_name='Изображение', on_delete=models.CASCADE)

    def __str__(self):
        return 'Сетка фоновых изображений DV'




