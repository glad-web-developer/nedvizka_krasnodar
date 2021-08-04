from django.db import models
from filer.fields.image import FilerImageField

from apps.nedvizka.CONST import CHOICES_NALICHIE_OTDELKI,  CHOICES_DA_NET, CHOICES_NALICHIE_VNESNEI_OTDELKI
from apps.nedvizka.models import Nedvizka


class DomProdaza(Nedvizka):
    class Meta:
        verbose_name = 'Дом - продажа'
        verbose_name_plural = '-Дома - продажа'
        ordering = ['-id']

    ploshad_uchastka = models.FloatField('Площадь участка (кв. м', null=True, blank=True)
    nalichie_gaza = models.BooleanField('Наличие газа в доме', default=False, null=True, blank=True, choices=CHOICES_DA_NET)
    blizost_so_shkoloi = models.BooleanField('Близость со школой', default=False, null=True, blank=True, choices=CHOICES_DA_NET)
    blizost_s_med = models.BooleanField('Близость с мед учереждением', default=False, null=True, blank=True, choices=CHOICES_DA_NET)
    blizost_s_metro = models.BooleanField('Близость с метро', default=False, null=True, blank=True, choices=CHOICES_DA_NET)
    nalichie_otdelki = models.IntegerField('Наличие внутренней отделки', default=1, null=True, blank=True, choices=CHOICES_NALICHIE_OTDELKI)
    nalichie_vnesheni_otdelki = models.IntegerField('Наличие внешней отделки', null=True, blank=True, default=1,
                                                    choices=CHOICES_NALICHIE_VNESNEI_OTDELKI)

    vodoprovod = models.BooleanField('Водопровод', null=True, blank=True, choices=CHOICES_DA_NET)
    electrichestvo = models.BooleanField('Электричество', null=True, blank=True, choices=CHOICES_DA_NET)
    ostanovki = models.CharField('Остановки', blank=True, null=True, max_length=255)


class FotoDomProdaza(models.Model):
    class Meta:
        verbose_name = 'Фото дома'
        verbose_name_plural = 'Фото дома'
        ordering = ['-index_sortirivki']

    dom = models.ForeignKey(DomProdaza, verbose_name='Дом', on_delete=models.CASCADE, null=True, blank=True,
                            related_name='foto_set')
    img = FilerImageField(verbose_name='Фото', on_delete=models.CASCADE)
    index_sortirivki = models.IntegerField('Индекс сортировки', default=0, help_text='Чем больше тем раньше выведет')

    def __str__(self):
        return f'Фото {self.img.url}'
