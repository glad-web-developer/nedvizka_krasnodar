from cms.models import  CMSPlugin
from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField, FilerFileField


class VideoPlayerJSPluginSetting(CMSPlugin):
    class Meta:
        verbose_name = 'Видео плеер JS'
        verbose_name_plural = 'Видео плеер JS'

    video = FilerFileField(verbose_name='Видео', on_delete=models.CASCADE)
    css_style = models.CharField(verbose_name='Стиль', blank=True, null=True, max_length=255)
    css_class = models.CharField(verbose_name='Класс', blank=True, null=True, max_length=255)
    height = models.CharField(verbose_name='Высота', blank=True, null=True, max_length=255)
    width = models.CharField(verbose_name='Ширина', blank=True, null=True, max_length=255)

    def __str__(self):
        return 'Видео плеер JS'





