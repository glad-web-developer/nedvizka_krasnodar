from cms.models import  CMSPlugin
from django.db import models
from filer.fields.image import FilerImageField


class GalereiaLvNaGlavnoiPluginSetting(CMSPlugin):
    class Meta:
        verbose_name = 'Галерея на главной'
        verbose_name_plural = 'Галерея на главной'

    def __str__(self):
        return 'Почему мы - список'

    img = models.ImageField(verbose_name='Изображение для PC', blank=True, null=True)
    img_phone = models.ImageField(verbose_name='Изображение для телефона', blank=True, null=True)




# class NapravleniaTrenirovokDvSetting(CMSPlugin):
#     class Meta:
#         verbose_name = 'Направления тренировок - ячейка'
#         verbose_name_plural = 'Направления тренировок - ячейка'
#
#     zagolovok = models.TextField('Заголовок', max_length=255, default='Заголовок')
#     img = models.ImageField(verbose_name='Изображение', null=True, blank=True)
#     ssilka = models.URLField('Ссылка', default='#')
#
#     def __str__(self):
#         return f'{self.zagolovok}'
#
