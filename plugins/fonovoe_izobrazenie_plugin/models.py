from cms.models import  CMSPlugin
from django.db import models
from filer.fields.image import FilerImageField
from easy_thumbnails.files import get_thumbnailer

class FonovoeIzobrazeniePluginSetting(CMSPlugin):
    class Meta:
        verbose_name = 'Фоновое изображение'
        verbose_name_plural = 'Фоновое изображение'

    def __str__(self):
        return 'Фоновое изображение'

    img = FilerImageField(verbose_name='Изображение', on_delete=models.CASCADE)

    width = models.PositiveIntegerField('Ширина при сжатие',  default=1600)
    height = models.PositiveIntegerField('Высота при сжатие', default=900)
    css_class = models.CharField('CSS класс', null=True, blank=True, max_length=255)
    css_style = models.CharField('CSS стиль', null=True, blank=True, max_length=1000)

    zatmenie_color = models.CharField('Затеменение изображения(r,g,b,a)', null=True, blank=True, max_length=255, default='0, 0, 0, 0.1')


    fix_razmer_width = models.BooleanField('Фиксированный размер ширины?', default=True)
    fix_razmer_height = models.BooleanField('Фиксированный размер высоты?', default=True)
    crop = models.BooleanField('Обрезать?', default=False)


    def get_szatoe_izobrazenie(self):
        options = {'size': (self.width, self.height), 'crop': True}
        thumb_url = get_thumbnailer(self.img).get_thumbnail(options).url
        return thumb_url


