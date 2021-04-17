from cms.models import CMSPlugin
from django.db import models


class SvoiStilIScriptPluginSetting(CMSPlugin):
    class Meta:
        verbose_name = 'Мой стиль'
        verbose_name_plural = 'Мой стиль'

    title = models.CharField('Название в структуре-дереве', null=True, blank=True, max_length=255)
    type = models.CharField('Тип', default='div', max_length=30, choices=(
        ('style', 'Стиль'),
        ('script', 'Скрипт'),
    ))

    text = models.TextField('Текст', null=True, blank=True)

    def get_short_description(self):
        if self.title:
            return self.title

        return f'#{self.id}'
