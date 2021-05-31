from django.contrib import admin

from apps.nedvizka.models import FotoDomProdaza, VideoDomProdaza, PanoramiDomProdaza, DomProdaza


class FotoDomProdazaInline(admin.TabularInline):
    model = FotoDomProdaza
    extra = 0
    classes = ['collapse']


class VideoDomProdazaInline(admin.TabularInline):
    model = VideoDomProdaza
    extra = 0
    classes = ['collapse']


class PanoramiDomProdazaInline(admin.TabularInline):
    model = PanoramiDomProdaza
    extra = 0
    classes = ['collapse']


class DomProdazaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nazvanie',
        'pokazivat',
        'price_bazovaia',
        'prrice_akzionnaia',
        'naselenii_punkt',
        'obshaia_ploshad',
        'eto_luchoe_prodlozenie',
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
        'naselenii_punkt',

    ]
    inlines = [FotoDomProdazaInline, VideoDomProdazaInline, PanoramiDomProdazaInline]

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
                ('price_bazovaia', 'prrice_akzionnaia',),
                ('naselenii_punkt', 'kordinati_na_karte'),
                ('obshaia_ploshad', 'ploshad_osnovnogo_doma'),
                ('nalichie_gaza', 'nalichie_otdelki', ),
                ('blizost_s_med', 'blizost_so_shkoloi', 'blizost_s_metro'),
            )
        }),
    ]


admin.site.register(DomProdaza, DomProdazaAdmin)
