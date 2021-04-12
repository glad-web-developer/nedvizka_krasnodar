from cms.models import CMSPlugin, Page
from django.db import models
from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField
from easy_thumbnails.files import get_thumbnailer


class SsilkaNavbarePluginSetting(CMSPlugin):
    class Meta:
        verbose_name = 'Навбарная ссылка'
        verbose_name_plural = 'Навбарная ссылка'

    def __str__(self):
        return 'Навбарная ссылка'

    title = models.CharField('Заголовок', null=False, blank=False, max_length=255)
    internal_link = models.ForeignKey(
        Page,
        verbose_name=('Внутренняя ссылка'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    external_link = models.CharField(
        verbose_name='Внешняя ссылка',
        blank=True,
        max_length=2040,
    )

    file_link = FilerFileField(
        verbose_name='Ссылка на файл',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )


    css_class = models.CharField('CSS класс', null=True, blank=True, max_length=255)
    css_style = models.CharField('CSS стиль', null=True, blank=True, max_length=1000)


    def get_short_description(self):
       return self.title

    def get_link(self):
        if self.internal_link:
            return self.internal_link

        if self.external_link:
            return self.external_link

        if self.file_link:
            return self.file_link

        return  '#'



