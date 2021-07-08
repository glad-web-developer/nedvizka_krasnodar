from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.nedvizka.models import FotoKvartiraPervichkaProdaza, VideoKvartiraPervichkaProdaza, \
    PanoramiKvartiraPervichkaProdaza, KvartiraPervichkaProdaza, KvartiraPervichkaArenda, FotoKvartiraPervichkaArenda, \
    VideoKvartiraPervichkaArenda, PanoramiKvartiraPervichkaArenda


class FotoKvartiraPervichkaProdazaInline(admin.TabularInline):
    model = FotoKvartiraPervichkaProdaza
    extra = 0
    classes = ['collapse']


class VideoKvartiraPervichkaProdazaInline(admin.TabularInline):
    model = VideoKvartiraPervichkaProdaza
    extra = 0
    classes = ['collapse']


class PanoramiKvartiraPervichkaProdazaInline(admin.TabularInline):
    model = PanoramiKvartiraPervichkaProdaza
    extra = 0
    classes = ['collapse']


class KvartiraPervichkaProdazaAdmin(ImportExportModelAdmin):
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
    inlines = [FotoKvartiraPervichkaProdazaInline, VideoKvartiraPervichkaProdazaInline, PanoramiKvartiraPervichkaProdazaInline]

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


admin.site.register(KvartiraPervichkaProdaza, KvartiraPervichkaProdazaAdmin)



class FotoKvartiraPervichkaArendaInline(admin.TabularInline):
    model = FotoKvartiraPervichkaArenda
    extra = 0
    classes = ['collapse']


class VideoKvartiraPervichkaArendaInline(admin.TabularInline):
    model = VideoKvartiraPervichkaArenda
    extra = 0
    classes = ['collapse']


class PanoramiKvartiraPervichkaArendaInline(admin.TabularInline):
    model = PanoramiKvartiraPervichkaArenda
    extra = 0
    classes = ['collapse']


class KvartiraPervichkaArendaAdmin(ImportExportModelAdmin):
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
    inlines = [FotoKvartiraPervichkaArendaInline, VideoKvartiraPervichkaArendaInline, PanoramiKvartiraPervichkaArendaInline]

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


# admin.site.register(KvartiraPervichkaArenda, KvartiraPervichkaArendaAdmin)
