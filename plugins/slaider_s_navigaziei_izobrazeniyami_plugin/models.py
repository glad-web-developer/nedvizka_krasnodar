from cms.models import CMSPlugin, Page
from django.db import models
from filer.fields.image import FilerImageField
from easy_thumbnails.files import get_thumbnailer


class SlaiderSNavigazieiIzobrazeniyamiPluginLvSetting(CMSPlugin):
    class Meta:
        verbose_name = 'Слайдер с навигацией изображениями'
        verbose_name_plural = 'Слайдер с навигацией изображениями'

    def __str__(self):
        return 'Слайдер с навигацией изображениями'

    title = models.CharField('Заголовок в структурном дереве', null=True, blank=True, max_length=255)
    css_class = models.CharField('CSS класс', null=True, blank=True, max_length=255)
    css_style = models.CharField('CSS стиль', null=True, blank=True, max_length=1000)

    width = models.IntegerField('Ширина при обрезке', default=1600)
    height = models.IntegerField('Высота при обрезке', default=900)

    def copy_relations(self, oldinstance):
        for instance in oldinstance.slaidi_set.all():
            instance.pk = None
            instance.slaider = self
            instance.save()

    def get_slaidi(self):
        return self.slaidi_set.select_related('img')


    def get_short_description(self):
       return f'{self.title or ""} {self.css_class or ""}'



class SlaiderSNavigazieiIzobrazeniyami(models.Model):
    class Meta:
        verbose_name = 'Слайд из слайдер с навигацией изображениями'
        verbose_name_plural = 'Слайд из слайдер с навигацией изображениями'
        ordering = ['-index_sortirovki',]

    slaider = models.ForeignKey(SlaiderSNavigazieiIzobrazeniyamiPluginLvSetting, related_name='slaidi_set', on_delete=models.CASCADE)

    title = models.CharField('Заголовок', null=True, blank=True, max_length=255)
    opisanie = models.TextField('Описание', null=True, blank=True)
    img = FilerImageField(verbose_name='Изображение', on_delete=models.CASCADE)
    index_sortirovki = models.IntegerField('Индекс сортировки', default=0, help_text='Чем больше, тем раньше отобразиться изображение')

    zatmenie_color =  models.CharField('Затеменение изображения(r,g,b,a)', null=True, blank=True, max_length=255, default='0, 0, 0, 0.1')

    def get_thumbnailer_img(self):
        height = self.img.height
        width = self.img.width
        thumbnailer = get_thumbnailer(self.img)
        return thumbnailer.get_thumbnail({'size': (width, height) })

    def __str__(self):
        return self.title