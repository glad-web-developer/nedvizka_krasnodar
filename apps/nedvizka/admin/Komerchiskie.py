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
    inlines = [FotoKomerchiskieProdazaInline, ]

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
    inlines = [FotoKomerchiskieArendaInline, ]

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


# admin.site.register(KomerchiskieArenda, KomerchiskieArendaAdmin)
