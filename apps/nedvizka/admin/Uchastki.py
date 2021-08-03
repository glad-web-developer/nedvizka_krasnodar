from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.nedvizka.models import  VideoUchactkiProdaza, \
    PanoramiUchactkiProdaza, UchactkiProdaza, UchactkiArenda, FotoUchactkiArenda, \
    VideoUchactkiArenda, PanoramiUchactkiArenda, FotoUchactkiProdaza


class FotoUchactkiProdazaInline(admin.TabularInline):
    model = FotoUchactkiProdaza
    extra = 0
    classes = ['collapse']


class VideoUchactkiProdazaInline(admin.TabularInline):
    model = VideoUchactkiProdaza
    extra = 0
    classes = ['collapse']


class PanoramiUchactkiProdazaInline(admin.TabularInline):
    model = PanoramiUchactkiProdaza
    extra = 0
    classes = ['collapse']


class UchactkiProdazaAdmin(ImportExportModelAdmin):
    list_display = [
        'id',
        'nazvanie',
        'pokazivat',
        'price_bazovaia',
        'prrice_akzionnaia',
        'naselenii_punkt',
        'obshaia_ploshad',

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

        'akzia',
        'naselenii_punkt',
    ]
    inlines = [FotoUchactkiProdazaInline, ]

    save_as = True
    save_on_top = True

    # fieldsets = [
    #     (None, {
    #         'fields': (
    #             'nazvanie',
    #             'slug',
    #             'previu',
    #             ('pokazivat', ),
    #             'opisaanaie',
    #             ('price_bazovaia', 'prrice_akzionnaia', ),
    #             ('naselenii_punkt', 'adres'),
    #             ('obshaia_ploshad'),
    #             ('nalichie_gaza', 'nalichie_otdelki', ),
    #             ('blizost_s_med', 'blizost_so_shkoloi', 'blizost_s_metro'),
    #         )
    #     }),
    # ]


admin.site.register(UchactkiProdaza, UchactkiProdazaAdmin)



class FotoUchactkiArendaInline(admin.TabularInline):
    model = FotoUchactkiArenda
    extra = 0
    classes = ['collapse']


class VideoUchactkiArendaInline(admin.TabularInline):
    model = VideoUchactkiArenda
    extra = 0
    classes = ['collapse']


class PanoramiUchactkiArendaInline(admin.TabularInline):
    model = PanoramiUchactkiArenda
    extra = 0
    classes = ['collapse']


class UchactkiArendaAdmin(ImportExportModelAdmin):
    list_display = [
        'id',
        'nazvanie',
        'pokazivat',
        'price_bazovaia',
        'prrice_akzionnaia',
        'naselenii_punkt',
        'obshaia_ploshad',

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

        'akzia',
        'naselenii_punkt',
    ]
    inlines = [FotoUchactkiArendaInline, VideoUchactkiArendaInline, PanoramiUchactkiArendaInline]

    save_as = True
    save_on_top = True

    fieldsets = [
        (None, {
            'fields': (
                'nazvanie',
                'slug',
                'previu',
                ('pokazivat', ),
                'opisaanaie',
                ('price_bazovaia', 'prrice_akzionnaia', ),
                ('naselenii_punkt', 'adres'),
                ('obshaia_ploshad'),
                ('nalichie_gaza', 'nalichie_otdelki', ),
                ('blizost_s_med', 'blizost_so_shkoloi', 'blizost_s_metro'),
            )
        }),
    ]


# admin.site.register(UchactkiArenda, UchactkiArendaAdmin)
