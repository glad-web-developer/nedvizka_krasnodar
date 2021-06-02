from django.contrib import admin

from apps.nedvizka.models import FotoKvartiraPervichkaProdaza, VideoKvartiraPervichkaProdaza, \
    PanoramiKvartiraPervichkaProdaza, KvartiraPervichkaProdaza


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


class KvartiraPervichkaProdazaAdmin(admin.ModelAdmin):
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
