from cms.models import  CMSPlugin
from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField


class OtziviLvPluginSetting(CMSPlugin):
    class Meta:
        verbose_name = 'Отзывы слайдер'
        verbose_name_plural = 'Отзывы слайдеры'

    title = models.CharField('Название в структуре-дереве', null=True, blank=True, max_length=255)
    css_class = models.CharField('Классы', null=True, blank=True, max_length=255)
    css_style = models.TextField('Стили', null=True, blank=True)


    # def get_otzivi(self):
    #     return self.otzivi_set.select_related('img')


    def __str__(self):
        return 'Отзывы слайдер'


    def get_short_description(self):
       return f'{self.title or ""} {self.css_class or ""}'

    def copy_relations(self, oldinstance):
        for instance in oldinstance.otzivi_set.all():
            instance.pk = None
            instance.otziv_slaider = self
            instance.save()



class OtzivDliaPlugina(models.Model):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзыв'

    otziv_slaider = models.ForeignKey(OtziviLvPluginSetting, verbose_name='Отзыв слайдер', on_delete=models.CASCADE, related_name='otzivi_set')
    avtor = models.CharField(verbose_name='Автор', max_length=255)
    opisanie = models.TextField(verbose_name='Отзыв')
    data = models.DateField(verbose_name='Дата и время', blank=True, null=True)
    ssilla = models.CharField('Ссылка', null=True, blank=True, max_length=500)
    ozenka = models.IntegerField('Оценка', default=0, choices=(
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ))

    def __str__(self):
        return self.avtor

    def get_ne_zapolninih_zvezd(self):
        return range(5 - self.ozenka)

    def get_zapolninih_zvezd(self):
        return range(self.ozenka)
