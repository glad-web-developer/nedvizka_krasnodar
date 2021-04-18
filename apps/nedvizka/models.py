from cms.models import PlaceholderField, CMSPlugin
from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from easy_thumbnails.files import get_thumbnailer
from filer.fields.image import FilerImageField


class Dom(models.Model):
    class Meta:
        verbose_name = 'Недвижка'
        verbose_name_plural = 'Недвижка'

    pokazivat = models.BooleanField('Показывать', default=True, choices=(
        (True, 'Показывать на сайте'),
        (False, 'Не показывать на сайте'),
    ))

    tip_operazii = models.IntegerField('Тип операции', choices=(
        (1, 'Продажа'),
        (2, 'Аренда'),
    ))

    nazvanie = models.CharField('Название', max_length=255)
    nomer = models.CharField('Номер(id объекта)', max_length=50)

    price_rub = models.FloatField('Цена руб', null=True, blank=True,
                                  help_text='Оставьте пустым, и сайт предложит пользователю запросить цену')
    price_dollor = models.FloatField('Цена $', null=True, blank=True,
                                     help_text='Оставьте пустым, и сайт предложит пользователю запросить цену')

    obshaia_ploshad = models.FloatField('Общая площадь (кв. м)', null=True, blank=True)

    raspolozenie_gorod = models.CharField('Город', null=True, blank=True, max_length=255)
    kordinati_na_karte = models.CharField('Кардинаты на карте', null=True, blank=True, max_length=255)

    ploshad_uchastka = models.FloatField('Площадь участка (соток)', null=True, blank=True, max_length=255)
    ploshad_osnovnogo_doma = models.FloatField('Площадь основного дома(кв.м)', null=True, blank=True, max_length=255)
    etaznost = models.IntegerField('Этажность', null=True, blank=True)
    kolvo_komnat = models.IntegerField('Количество комнат', null=True, blank=True)
    kolvo_spalen = models.IntegerField('Количество спален', null=True, blank=True)
    kolvo_sanuzlov = models.IntegerField('Количество санузлов', null=True, blank=True)
    otdelka = models.CharField('Отделка', null=True, blank=True, max_length=255)
    mebel = models.BooleanField('Мебель', null=True, blank=True, max_length=255, default=False, choices=(
        (True, 'Есть'),
        (False, 'Нет'),
    ))

    bassein = models.CharField('Бассейн', null=True, blank=True, max_length=255)
    zona_barbeku = models.CharField('Зона барбекю', null=True, blank=True, max_length=255)
    rastoianie_do_moria = models.CharField('Расстояние до моря', null=True, blank=True, max_length=255)
    rastoianie_do_goroda = models.CharField('Расстояние до города', null=True, blank=True, max_length=255)

    opisaanaie_kratkoe = models.TextField('Краткое описание для страницы поиска', null=True, blank=True)

    tip_oformlenia_stranizi_obiekta = models.CharField('Тип оформления страницы объекта', null=True, blank=True,
                                                       max_length=50, default='sablon', choices=(
            ('sablon', 'Шаблонный(стандартный)'),
            ('proizvolni', 'Произвольный(можно самому настроить оформление)'),
        ))
    opisaanaie = models.TextField('Описание для страницы детальной информации', null=True, blank=True,
                                  help_text='Будет выводиться только если выбран шаблонное оформление страницы объекта')
    iframe_panorami = models.TextField('Описание для страницы детальной информации', null=True, blank=True,
                                       help_text='Будет выводиться только если выбран шаблонное оформление страницы объекта')
    video = models.TextField('Ссылка на видео youtube', null=True, blank=True,
                                       help_text='Будет выводиться только если выбран шаблонное оформление страницы объекта')

    def __str__(self):
        try:
            return f'{self.nomer} - {self.nazvanie}'
        except Exception:
            return ''

class FotoDomov(models.Model):
    class Meta:
        verbose_name = 'Фото домов'
        verbose_name_plural = 'Фото домов'

    dom = models.ForeignKey(Dom, verbose_name='Дом', on_delete=models.CASCADE, null=True, blank=True)
    img = FilerImageField(verbose_name='Превью', )

# class Novost(models.Model):
#     class Meta:
#         verbose_name = 'Новость'
#         verbose_name_plural = 'Новости'
#         ordering = ['-data_sozdania', ]
#
#     title = models.CharField('Заголовок', max_length = 255)
#     img = FilerImageField(verbose_name='Превью',)
#     data_sozdania = models.DateField('Дата новости')
#     dlinnoe_opisanie = HTMLField('Текст новости', blank=True, null=True,)
#     anotazia = models.TextField('Анотация', help_text='До 200 символов', blank=True, null=True, max_length=200)
#
#     def get_thumbnailer_img(self):
#         thumbnailer = get_thumbnailer(self.img)
#         return thumbnailer.get_thumbnail({'size': (400, 300), 'crop': True, })
#
#
#     def __str__(self):
#         return self.title
#
#
# class NovostImg(models.Model):
#     class Meta:
#         verbose_name = 'Фото новости'
#         verbose_name_plural = 'Фото новости'
#
#     novost = models.ForeignKey(Novost, verbose_name='Новость', on_delete=models.CASCADE, related_name='fotki')
#     img = FilerImageField(verbose_name='Фото', )
#
#     def get_thumbnailer_img(self):
#         thumbnailer = get_thumbnailer(self.img)
#         return thumbnailer.get_thumbnail({'size': (250, 200), 'crop': True, })
#
#     def __str__(self):
#         return ''
