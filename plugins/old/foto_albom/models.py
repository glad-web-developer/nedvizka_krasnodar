from cms.models import  CMSPlugin
from django.db import models
from django.utils.safestring import mark_safe
from easy_thumbnails.files import get_thumbnailer
from filer.fields.image import FilerImageField


class FotoAlbomPluginSetting(CMSPlugin):
    class Meta:
        verbose_name = 'Фотоальбом'
        verbose_name_plural = 'Фотоальбом'

    width = models.PositiveIntegerField('Ширина при обрезке', default=250, help_text='Если сомневаетесь, то не меняйте=}')
    height = models.PositiveIntegerField('Высота при обрезке', default=150, help_text='Если сомневаетесь, то не меняйте=}')

    def copy_relations(self, oldinstance):
        for foto in oldinstance.foto_iz_alboma.all():
            foto.pk = None
            foto.id = None
            foto.fotoalbom = self
            foto.save()

    def __str__(self):
        return ''


class FotoIzAlboma(models.Model):
    class Meta:
        verbose_name = 'Фото из фотоальбома'
        verbose_name_plural = 'Фото из фотоальбома'
        ordering = ['-index_sortirovki',]

    fotoalbom = models.ForeignKey(FotoAlbomPluginSetting, related_name='foto_iz_alboma', on_delete=models.CASCADE)

    img = FilerImageField(verbose_name='Фото из фотоальбома', related_name='img_iz_alboma', on_delete=models.CASCADE)
    index_sortirovki = models.IntegerField('Индекс сортировки', default=0, help_text='Чем больше, тем раньше отобразиться фото в альбоме')

    def get_thumbnailer_img(self):
        height = self.fotoalbom.height
        width = self.fotoalbom.width
        thumbnailer = get_thumbnailer(self.img)
        return thumbnailer.get_thumbnail({'size': (width, height), 'crop': ',30', })

    def __str__(self):
        return ''
    #     thumbnailer = get_thumbnailer(self.img)
    #     thumb = thumbnailer.get_thumbnail({'size': (50, 50), 'crop': True})
    #     return mark_safe('<img class="img-fluid" src="{}" >'.format(thumb.url))
