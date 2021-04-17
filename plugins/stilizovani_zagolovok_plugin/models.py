from cms.models import CMSPlugin
from django.db import models


class StilizovaniZagolovokPluginSetting(CMSPlugin):
    class Meta:
        verbose_name = 'Стилизованный заголовок'
        verbose_name_plural = 'Стилизованный заголовок'

    tag = models.CharField('Тег', default='span', max_length=30, )
    text = models.TextField('Текст')
    css_class = models.CharField('Прочие классы', max_length=255, null=True, blank=True )
    all_style = models.TextField('col стили', null=True, blank=True)
    sm_style = models.TextField('sm стили', null=True, blank=True)
    md_style = models.TextField('md стили', null=True, blank=True)
    lg_style = models.TextField('lg стили', null=True, blank=True)
    xl_style = models.TextField('xl стили', null=True, blank=True)

    def get_short_description(self):
        if self.text:
            return self.text

        return f'#{self.id}'
