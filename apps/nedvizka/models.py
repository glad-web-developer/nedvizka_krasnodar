from cms.models import PlaceholderField, CMSPlugin
from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from easy_thumbnails.files import get_thumbnailer
from filer.fields.image import FilerImageField


class Dom(models.Model):
    class Meta:
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'

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

    slug = models.SlugField('Ссылка', max_length=255, null=True, blank=True )


    previu = FilerImageField(verbose_name='Превью', null=True, blank=True, on_delete=models.CASCADE)

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
    opisaanaie = HTMLField('Описание для страницы детальной информации', null=True, blank=True,
                                  help_text='Будет выводиться только если выбран шаблонное оформление страницы объекта')
    iframe_panorami = models.CharField('Код панорами', null=True, blank=True, max_length=1000,
                                       help_text='Будет выводиться только если выбран шаблонное оформление страницы объекта')
    video = models.CharField('Ссылка на видео youtube', null=True, blank=True, max_length=1000,
                                       help_text='Будет выводиться только если выбран шаблонное оформление страницы объекта')

    def get_foto_set(self):
        return self.foto_set.select_related('img')

    def get_colvo_img(self):
        return  self.foto_set.select_related('img') .count()

    def __str__(self):
        try:
            return f'{self.nomer} - {self.nazvanie}'
        except Exception:
            return ''

    def get_url(self):
        if self.slug:
            return self.slug
        return self.id

class FotoDomov(models.Model):
    class Meta:
        verbose_name = 'Фото дома'
        verbose_name_plural = 'Фото дома'
        ordering = ['-index_sortirivki']

    dom = models.ForeignKey(Dom, verbose_name='Дом', on_delete=models.CASCADE, null=True, blank=True, related_name='foto_set')
    img = FilerImageField(verbose_name='Фото', on_delete=models.CASCADE)
    index_sortirivki = models.IntegerField('Индекс сортировки', default=0, help_text='Чем больше тем раньше выведет')

    def __str__(self):
        return f'Фото {self.img.url}'

class NedvizkaSpisokObiectovPluginPluginSetting(CMSPlugin):
    class Meta:
        verbose_name = 'Недвижка. Список объектов'
        verbose_name_plural = 'Недвижка. Список объектов'

    def __str__(self):
        return 'Недвижка. Список объектов'

    tip_nedvizki = models.CharField('Тип недвижки', max_length=255, choices=(
        ('dom_prodaza', 'Дом-продажа'),
        ('dom_arenda', 'Дом-аренда'),
    ))

    obiectov_na_stranize = models.IntegerField('Выводить по ', default=10)

    css_class = models.CharField('CSS класс', null=True, blank=True, max_length=255)
    css_style = models.CharField('CSS стиль', null=True, blank=True, max_length=1000)

    def get_short_description(self):
        tip_nedvizki = self.tip_nedvizki or '-'
        obiectov_na_stranize = self.obiectov_na_stranize or '-'
        return f'{tip_nedvizki} (по {obiectov_na_stranize} шт.)'



class NedvizkaIzbranoePluginSetting(CMSPlugin):
    class Meta:
        verbose_name = 'Недвижка. Избранное'
        verbose_name_plural = 'Недвижка. Избранное'

    def __str__(self):
        return 'Недвижка. Избранное'

    css_class = models.CharField('CSS класс', null=True, blank=True, max_length=255)
    css_style = models.CharField('CSS стиль', null=True, blank=True, max_length=1000)




class NedvizkaPanelUpravleniaPluginSetting(CMSPlugin):
    class Meta:
        verbose_name = 'Недвижка. Избранное'
        verbose_name_plural = 'Недвижка. Избранное'

    def __str__(self):
        return 'Недвижка. Избранное'

    pokazat_kartu = models.BooleanField('Показывать карту', default=True)
    pokazat_sortirovku = models.BooleanField('Показывать сортировку', default=True)
    css_class = models.CharField('CSS класс', null=True, blank=True, max_length=255)
    css_style = models.CharField('CSS стиль', null=True, blank=True, max_length=1000)



