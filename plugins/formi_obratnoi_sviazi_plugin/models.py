from cms.models import  CMSPlugin
from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField


class FormaObratnoiSviaziSetting(CMSPlugin):
    class Meta:
        verbose_name = 'Форма обратной связи'
        verbose_name_plural = 'Форма обратной связи'

    zagolovok = models.TextField('Заголовок', blank=True, null=True)
    podpis = HTMLField('Подпись', blank=True, null=True,)
    img = FilerImageField(verbose_name='Изображение', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return 'Форма обратной связи'


class ZakazanieZvonki(CMSPlugin):
    class Meta:
        verbose_name = 'Заказаные обратные звонки'
        verbose_name_plural = 'Заказаные обратные звонки'

    name = models.CharField('Имя', max_length=255, null=True, blank=True)
    phone = models.CharField('Телефон', max_length=255, null=True, blank=True)
    data = models.DateTimeField('Дата', auto_now_add=True, editable=False)
    perezvonili = models.BooleanField('Перезвонили?', default=False)