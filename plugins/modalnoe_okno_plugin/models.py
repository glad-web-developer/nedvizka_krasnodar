from cms.models import  CMSPlugin
from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField


class ModalnoeOknoPluginSetting(CMSPlugin):
    class Meta:
        verbose_name = 'Модальное окно'
        verbose_name_plural = 'Модальное окно'

    yakor = models.CharField('Якорь', max_length=255, null=True, blank=True, help_text='у кнопки не забыть data-toggle="modal" data-target="#example"')
    zagolovok = models.CharField('Заголовок', max_length=255, null=True, blank=True)

    def get_short_description(self):
        return self.yakor