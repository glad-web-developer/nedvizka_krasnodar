from cms.models import  CMSPlugin
from django.db import models
from filer.fields.image import FilerImageField


class PochemuMiLvPluginSetting(CMSPlugin):
    class Meta:
        verbose_name = 'Почему мы - список'
        verbose_name_plural = 'Почему мы - список'

    def __str__(self):
        return 'Почему мы - список'




class PochemuMiDvVideoPluginSetting(CMSPlugin):
    class Meta:
        verbose_name = 'Почему мы - ячейка'
        verbose_name_plural = 'Почему мы - ячейка'

    zagolovok = models.TextField('Заголовок', max_length=255, default='Заголовок')
    img = models.ImageField(verbose_name='Изображение', null=True, blank=True)

    def __str__(self):
        return f'{self.zagolovok}'

