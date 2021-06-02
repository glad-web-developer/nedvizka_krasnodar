from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.nedvizka.models import  VideoKvartiraVtorichkaProdaza, \
    PanoramiKvartiraVtorichkaProdaza, KvartiraVtorichkaProdaza, KvartiraVtorichkaArenda, FotoKvartiraVtorichkaArenda, \
    VideoKvartiraVtorichkaArenda, PanoramiKvartiraVtorichkaArenda, FotoKvartiraVtorichkaProdaza


class FotoKvartiraVtorichkaProdazaInline(admin.TabularInline):
    model = FotoKvartiraVtorichkaProdaza
    extra = 0
    classes = ['collapse']


class VideoKvartiraVtorichkaProdazaInline(admin.TabularInline):
    model = VideoKvartiraVtorichkaProdaza
    extra = 0
    classes = ['collapse']


class PanoramiKvartiraVtorichkaProdazaInline(admin.TabularInline):
    model = PanoramiKvartiraVtorichkaProdaza
    extra = 0
    classes = ['collapse']


class KvartiraVtorichkaProdazaAdmin(ImportExportModelAdmin):
    list_display = [
        'id',
        'nazvanie',
        'pokazivat',
        'price_bazovaia',
        'prrice_akzionnaia',
        'naselenii_punkt',
        'obshaia_ploshad',
        'eto_luchoe_prodlozenie',
        'akzia'
    ]
    search_fields = [
        'id',
        'nazvanie',
        'price_bazovaia',
        'prrice_akzionnaia',
    ]
    list_filter = [
        'pokazivat',
        'eto_luchoe_prodlozenie',
        'akzia',
        'naselenii_punkt',
    ]
    inlines = [FotoKvartiraVtorichkaProdazaInline, VideoKvartiraVtorichkaProdazaInline, PanoramiKvartiraVtorichkaProdazaInline]

    save_as = True
    save_on_top = True

    fieldsets = [
        (None, {
            'fields': (
                'nazvanie',
                'slug',
                'previu',
                ('pokazivat', 'eto_luchoe_prodlozenie',),
                'opisaanaie',
                ('price_bazovaia', 'prrice_akzionnaia', ),
                ('naselenii_punkt', 'adres', 'kordinati_na_karte'),
                ('obshaia_ploshad'),
                ('nalichie_gaza', 'nalichie_otdelki', ),
                ('blizost_s_med', 'blizost_so_shkoloi', 'blizost_s_metro'),
            )
        }),
    ]


admin.site.register(KvartiraVtorichkaProdaza, KvartiraVtorichkaProdazaAdmin)



class FotoKvartiraVtorichkaArendaInline(admin.TabularInline):
    model = FotoKvartiraVtorichkaArenda
    extra = 0
    classes = ['collapse']


class VideoKvartiraVtorichkaArendaInline(admin.TabularInline):
    model = VideoKvartiraVtorichkaArenda
    extra = 0
    classes = ['collapse']


class PanoramiKvartiraVtorichkaArendaInline(admin.TabularInline):
    model = PanoramiKvartiraVtorichkaArenda
    extra = 0
    classes = ['collapse']


class KvartiraVtorichkaArendaAdmin(ImportExportModelAdmin):
    list_display = [
        'id',
        'nazvanie',
        'pokazivat',
        'price_bazovaia',
        'prrice_akzionnaia',
        'naselenii_punkt',
        'obshaia_ploshad',
        'eto_luchoe_prodlozenie',
        'akzia'
    ]
    search_fields = [
        'id',
        'nazvanie',
        'price_bazovaia',
        'prrice_akzionnaia',
    ]
    list_filter = [
        'pokazivat',
        'eto_luchoe_prodlozenie',
        'akzia',
        'naselenii_punkt',
    ]
    inlines = [FotoKvartiraVtorichkaArendaInline, VideoKvartiraVtorichkaArendaInline, PanoramiKvartiraVtorichkaArendaInline]

    save_as = True
    save_on_top = True

    fieldsets = [
        (None, {
            'fields': (
                'nazvanie',
                'slug',
                'previu',
                ('pokazivat', 'eto_luchoe_prodlozenie',),
                'opisaanaie',
                ('price_bazovaia', 'prrice_akzionnaia', ),
                ('naselenii_punkt', 'adres', 'kordinati_na_karte'),
                ('obshaia_ploshad'),
                ('nalichie_gaza', 'nalichie_otdelki', ),
                ('blizost_s_med', 'blizost_so_shkoloi', 'blizost_s_metro'),
            )
        }),
    ]


admin.site.register(KvartiraVtorichkaArenda, KvartiraVtorichkaArendaAdmin)
