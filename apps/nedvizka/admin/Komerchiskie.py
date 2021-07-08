from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.nedvizka.models import  VideoKomerchiskieProdaza, \
    PanoramiKomerchiskieProdaza, KomerchiskieProdaza, KomerchiskieArenda, FotoKomerchiskieArenda, \
    VideoKomerchiskieArenda, PanoramiKomerchiskieArenda, FotoKomerchiskieProdaza


class FotoKomerchiskieProdazaInline(admin.TabularInline):
    model = FotoKomerchiskieProdaza
    extra = 0
    classes = ['collapse']


class VideoKomerchiskieProdazaInline(admin.TabularInline):
    model = VideoKomerchiskieProdaza
    extra = 0
    classes = ['collapse']


class PanoramiKomerchiskieProdazaInline(admin.TabularInline):
    model = PanoramiKomerchiskieProdaza
    extra = 0
    classes = ['collapse']


class KomerchiskieProdazaAdmin(ImportExportModelAdmin):
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
    inlines = [FotoKomerchiskieProdazaInline, VideoKomerchiskieProdazaInline, PanoramiKomerchiskieProdazaInline]

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


admin.site.register(KomerchiskieProdaza, KomerchiskieProdazaAdmin)



class FotoKomerchiskieArendaInline(admin.TabularInline):
    model = FotoKomerchiskieArenda
    extra = 0
    classes = ['collapse']


class VideoKomerchiskieArendaInline(admin.TabularInline):
    model = VideoKomerchiskieArenda
    extra = 0
    classes = ['collapse']


class PanoramiKomerchiskieArendaInline(admin.TabularInline):
    model = PanoramiKomerchiskieArenda
    extra = 0
    classes = ['collapse']


class KomerchiskieArendaAdmin(ImportExportModelAdmin):
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
    inlines = [FotoKomerchiskieArendaInline, VideoKomerchiskieArendaInline, PanoramiKomerchiskieArendaInline]

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


# admin.site.register(KomerchiskieArenda, KomerchiskieArendaAdmin)
