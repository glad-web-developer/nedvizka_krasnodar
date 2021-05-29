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
    list_display = ['nomer', 'nazvanie', 'pokazivat', 'price_dollor']
    search_fields = ['id', 'nomer', 'nazvanie', 'pokazivat', 'price_dollor']
    list_filter = ['pokazivat', 'filter_peshai_dostupnost_k_pliazu', 'filter_kotedzni_poselok', 'filter_bassein',
                   'filter_vid_na_moria']
    inlines = [FotoDomProdazaInline, VideoDomProdazaInline, PanoramiDomProdazaInline]

    save_as = True
    save_on_top = True

    fieldsets = [
        (None, {
            'fields': (
                'nomer',
                'nazvanie',
                'pokazivat',
                'previu',
                ('price_dollor', 'price_rub',),
                ('raspolozenie_gorod', 'kordinati_na_karte'),
                ('obshaia_ploshad', 'ploshad_uchastka', 'ploshad_osnovnogo_doma',  'spalen',),

            )
        }),

        ('Фильтры', {

            'fields': (
                'filter_peshai_dostupnost_k_pliazu',
                'filter_kotedzni_poselok',
                'filter_bassein',
                'filter_vid_na_moria',
            )
        }),

        ('Описание и таблица параметров', {
            'classes': ('collapse',),
            'fields': (
                'opisaanaie_kratkoe',
                'opisaanaie',
                'tabliza_harakterisstik',
            )
        }),



    ]


admin.site.register(DomProdaza, DomProdazaAdmin)
