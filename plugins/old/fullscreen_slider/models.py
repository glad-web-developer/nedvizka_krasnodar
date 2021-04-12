from cms.models import  CMSPlugin
from django.db import models
from filer.fields.image import FilerImageField


class FullscreenSliderLvPluginSetting(CMSPlugin):
    class Meta:
        verbose_name = 'Полноэкранный слайдер'
        verbose_name_plural = 'Полноэкранный слайдер'

    def __str__(self):
        return 'Полноэкранный слайдер'




class FullscreenSliderDvVideoPluginSetting(CMSPlugin):
    class Meta:
        verbose_name = 'Слайд видео'
        verbose_name_plural = 'Слайд видео'

    def __str__(self):
        return f'Слайд видео'

