from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.nedvizka.models import  VideoNezelieProdaza, \
    PanoramiNezelieProdaza, NezelieProdaza, NezelieArenda, FotoNezelieArenda, \
    VideoNezelieArenda, PanoramiNezelieArenda, FotoNezelieProdaza


class FotoNezelieProdazaInline(admin.TabularInline):
    model = FotoNezelieProdaza
    extra = 0
    classes = ['collapse']


class VideoNezelieProdazaInline(admin.TabularInline):
    model = VideoNezelieProdaza
    extra = 0
    classes = ['collapse']


class PanoramiNezelieProdazaInline(admin.TabularInline):
    model = PanoramiNezelieProdaza
    extra = 0
    classes = ['collapse']


class NezelieProdazaAdmin(ImportExportModelAdmin):
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
    inlines = [FotoNezelieProdazaInline, VideoNezelieProdazaInline, PanoramiNezelieProdazaInline]

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


admin.site.register(NezelieProdaza, NezelieProdazaAdmin)



class FotoNezelieArendaInline(admin.TabularInline):
    model = FotoNezelieArenda
    extra = 0
    classes = ['collapse']


class VideoNezelieArendaInline(admin.TabularInline):
    model = VideoNezelieArenda
    extra = 0
    classes = ['collapse']


class PanoramiNezelieArendaInline(admin.TabularInline):
    model = PanoramiNezelieArenda
    extra = 0
    classes = ['collapse']


class NezelieArendaAdmin(ImportExportModelAdmin):
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
    inlines = [FotoNezelieArendaInline, VideoNezelieArendaInline, PanoramiNezelieArendaInline]

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


admin.site.register(NezelieArenda, NezelieArendaAdmin)
