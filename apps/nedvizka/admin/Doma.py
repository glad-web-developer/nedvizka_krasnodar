from django.contrib import admin

from apps.nedvizka.models import FotoDomProdaza, VideoDomProdaza, PanoramiDomProdaza, DomProdaza, FotoDomArenda, \
    VideoDomArendda, PanoramiDomaArenda, DomArenda

from import_export.admin import ImportExportModelAdmin



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


class DomProdazaAdmin(ImportExportModelAdmin):
    list_display = [
        'id',
        'nazvanie',
        'pokazivat',
        'price_bazovaia',
        'prrice_akzionnaia',
        'naselenii_punkt',
        'obshaia_ploshad',
        # 'eto_luchoe_prodlozenie',
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
        # 'eto_luchoe_prodlozenie',
        'akzia',
        'naselenii_punkt',
    ]
    inlines = [FotoDomProdazaInline,]

    save_as = True
    save_on_top = True

    fieldsets = [
        (None, {
            'fields': (
                'nazvanie',
                'slug',
                'previu',
                'pokazivat',
                'opisaanaie',
                ('price_bazovaia', 'prrice_akzionnaia', ),
                ('naselenii_punkt', 'adres'),
                ('obshaia_ploshad', 'ploshad_osnovnogo_doma'),
                ('nalichie_gaza', 'nalichie_otdelki', ),
                ('blizost_s_med', 'blizost_so_shkoloi', 'blizost_s_metro'),
            )
        }),
    ]


admin.site.register(DomProdaza, DomProdazaAdmin)


class FotoDomArendaInline(admin.TabularInline):
    model = FotoDomArenda
    extra = 0
    classes = ['collapse']


class VideoDomArendaInline(admin.TabularInline):
    model = VideoDomArendda
    extra = 0
    classes = ['collapse']


class PanoramiDomArendaInline(admin.TabularInline):
    model = PanoramiDomaArenda
    extra = 0
    classes = ['collapse']


class DomArendaAdmin(ImportExportModelAdmin):
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
    inlines = [FotoDomArendaInline, VideoDomArendaInline, PanoramiDomArendaInline]

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
                ('obshaia_ploshad', 'ploshad_osnovnogo_doma'),
                ('nalichie_gaza', 'nalichie_otdelki', ),
                ('blizost_s_med', 'blizost_so_shkoloi', 'blizost_s_metro'),
            )
        }),
    ]


# admin.site.register(DomArenda, DomArendaAdmin)
