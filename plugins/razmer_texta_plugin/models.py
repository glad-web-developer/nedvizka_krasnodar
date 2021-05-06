from cms.models import CMSPlugin
from django.db import models
from djangocms_text_ckeditor.fields import HTMLField


class RazmerTextaPluginSetting(CMSPlugin):
    class Meta:
        verbose_name = 'Мой стиль'
        verbose_name_plural = 'Мой стиль'

    text = models.TextField('Текст')

    col_size = models.CharField('col размер', help_text='с указанием px/pt и прочего', null=True, blank=True, max_length=255)
    sm_size = models.CharField('sm размер', help_text='с указанием px/pt и прочего', null=True, blank=True, max_length=255)
    md_size = models.CharField('md размер', help_text='с указанием px/pt и прочего', null=True, blank=True, max_length=255)
    lg_size = models.CharField('lg размер', help_text='с указанием px/pt и прочего', null=True, blank=True, max_length=255)
    xl_size = models.CharField('xl размер', help_text='с указанием px/pt и прочего', null=True, blank=True, max_length=255)
    css_class = models.CharField('Прочие классы', max_length=255, null=True, blank=True)
    all_style = models.TextField('Прочие стили стили', null=True, blank=True)

    def get_short_description(self):
        return self.text[0:50]
