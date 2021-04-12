from cms.models import  CMSPlugin
from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField


class TreneraLvSetting(CMSPlugin):
    class Meta:
        verbose_name = 'Тренера - список'
        verbose_name_plural = 'Тренера - список'

    def __str__(self):
        return 'Тренера - список'



class TreneraDvSetting(CMSPlugin):
    class Meta:
        verbose_name = 'Тренера - ячейка'
        verbose_name_plural = 'Тренера - ячейка'

    fio = models.CharField('ФИО', max_length=255, default='-')
    img = models.ImageField(verbose_name='Изображение', null=True, blank=True)
    ssilka = models.CharField('Ссылка', default='#', max_length=1000)
    opisanie = HTMLField(verbose_name='Описание', blank=True, null=True)


    def __str__(self):
        return f'{self.fio}'



