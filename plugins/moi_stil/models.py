from cms.models import CMSPlugin
from django.db import models


class MoiStilPluginSetting(CMSPlugin):
    class Meta:
        verbose_name = 'Мой стиль'
        verbose_name_plural = 'Мой стиль'

    title = models.CharField('Название в структуре-дереве', null=True, blank=True, max_length=255)
    css_classs = models.CharField('Классы', null=True, blank=True, max_length=255)
    css_style = models.TextField('Стили', null=True, blank=True)
    tag_type = models.CharField('Тег', default='div', max_length=255)

    def get_short_description(self):
        if self.title:
            text = f'{self.title}: {self.tag_type}'
        else:
            text = self.tag_type

        if self.css_classs:
            text += f' ({self.css_classs})'
        return text
