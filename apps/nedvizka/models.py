from cms.models import PlaceholderField, CMSPlugin
from django.db import models
from django.utils.safestring import mark_safe
from djangocms_text_ckeditor.fields import HTMLField
from easy_thumbnails.files import get_thumbnailer
from filer.fields.image import FilerImageField


# *** дома продажа ***

class DomProdaza(models.Model):
    class Meta:
        verbose_name = 'Дом - продажа'
        verbose_name_plural = 'Дома - продажа'

    pokazivat = models.BooleanField('Показывать', default=True, choices=(
        (True, 'Показывать на сайте'),
        (False, 'Не показывать на сайте'),
    ))

    nazvanie = models.CharField('Название', max_length=255)
    nomer = models.CharField('Номер(id объекта)', max_length=50)
    slug = models.SlugField('Ссылка', max_length=255, null=True, blank=True)
    previu = FilerImageField(verbose_name='Превью', null=True, blank=True, on_delete=models.CASCADE)
    price_rub = models.FloatField('Цена руб', null=True, blank=True,
                                  help_text='Оставьте пустым, и сайт предложит пользователю запросить цену')
    price_dollor = models.FloatField('Цена $', null=True, blank=True,
                                     help_text='Оставьте пустым, и сайт предложит пользователю запросить цену')
    obshaia_ploshad = models.FloatField('Общая площадь (кв. м)', null=True, blank=True)
    raspolozenie_gorod = models.CharField('Город', null=True, blank=True, max_length=255)
    kordinati_na_karte = models.CharField('Координаты на карте', null=True, blank=True, max_length=255, help_text='Например "44.533249, 33.455248" без кавычек (https://snipp.ru/tools/address-coord)')
    ploshad_uchastka = models.FloatField('Площадь участка (соток)', null=True, blank=True, max_length=255)
    ploshad_osnovnogo_doma = models.FloatField('Площадь основного дома(кв.м)', null=True, blank=True, max_length=255)

    spalen = models.IntegerField('Спални (кол-во)', null=True, blank=True)

    tabliza_harakterisstik = HTMLField('Таблица характеристик', null=True, blank=True)

    opisaanaie_kratkoe = models.TextField('Краткое описание для страницы поиска', null=True, blank=True)
    opisaanaie = HTMLField('Описание для страницы детальной информации', null=True, blank=True,
                           help_text='Будет выводиться только если выбран шаблонное оформление страницы объекта')

    filter_peshai_dostupnost_k_pliazu = models.BooleanField('Пешая доступность к пляжу', default=False)
    filter_kotedzni_poselok = models.BooleanField('Коттеджный поселок', default=False)
    filter_bassein = models.BooleanField('Бассейн', default=False)
    filter_vid_na_moria = models.BooleanField('Вид на моря', default=False)

    def get_foto_set(self):
        return self.foto_set.select_related('img')

    def get_colvo_img(self):
        return self.foto_set.select_related('img').count()

    def __str__(self):
        try:
            return f'{self.nomer} - {self.nazvanie}'
        except Exception:
            return ''

    def get_url(self):
        if self.slug:
            return self.slug
        return self.id


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


class VideoDomProdaza(models.Model):
    class Meta:
        verbose_name = 'Видео дома'
        verbose_name_plural = 'Видео дома'
        ordering = ['-index_sortirivki']

    dom = models.ForeignKey(DomProdaza, verbose_name='Дом', on_delete=models.CASCADE, null=True, blank=True,
                            related_name='video_set')
    video = models.TextField('Iframe код видео',
                             help_text='Будет выводиться только если выбран шаблонное оформление страницы объекта')
    index_sortirivki = models.IntegerField('Индекс сортировки', default=0, help_text='Чем больше тем раньше выведет')

    def __str__(self):
        return str(self.id)

class PanoramiDomProdaza(models.Model):
    class Meta:
        verbose_name = 'Панорамы домов'
        verbose_name_plural = 'Панорамы домов'
        ordering = ['-index_sortirivki']

    dom = models.ForeignKey(DomProdaza, verbose_name='Дом', on_delete=models.CASCADE, null=True, blank=True,
                            related_name='panorami_set')
    iframe_code = models.TextField('iframe код',
                                   help_text='Будет выводиться только если выбран шаблонное оформление страницы объекта')
    index_sortirivki = models.IntegerField('Индекс сортировки', default=0, help_text='Чем больше тем раньше выведет')

    def __str__(self):
        return str(self.id)

# -------------

