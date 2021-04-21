from django.contrib import admin

from apps.nedvizka.models import FotoDomov, Dom, VideoDomov, PanoramiDomov


class FotoDomovInline(admin.TabularInline):
    model = FotoDomov
    extra = 0

class VideoDomovInline(admin.TabularInline):
    model = VideoDomov
    extra = 0

class PanoramiDomovInline(admin.TabularInline):
    model = PanoramiDomov
    extra = 0


class DomAdmin(admin.ModelAdmin):
    list_display = ['nomer','nazvanie', 'pokazivat', 'tip_operazii', 'price_dollor']
    search_fields = ['id','nomer','nazvanie', 'pokazivat', 'tip_operazii', 'price_dollor']
    list_filter  = ['tip_operazii','pokazivat']
    inlines = [FotoDomovInline, VideoDomovInline, PanoramiDomovInline]

    save_as = True
    save_on_top = True

    fieldsets = [
        (None, {
            'fields': (
                'nomer',
                'nazvanie',
                ('pokazivat', 'tip_operazii',),
                 'previu',
                 ('price_dollor','price_rub',),

            )
        }),
        ('Описание',{
            'classes': ('collapse',),
            'fields':(
                'tip_oformlenia_stranizi_obiekta',
                'opisaanaie_kratkoe',
                'opisaanaie',
            )
        }),
        (('Расположение и площадь'), {
            'classes': ('collapse',),
            'fields': (
                ('raspolozenie_gorod', 'kordinati_na_karte'),
                'obshaia_ploshad',
                ('ploshad_uchastka', 'ploshad_osnovnogo_doma'),
                ('rastoianie_do_moria', 'rastoianie_do_goroda'),
            ),
        }),

        (('Параметры дома'), {
            'classes': ('collapse',),
            'fields': (
                ('etaznost', 'kolvo_komnat'),
                ('kolvo_spalen', 'kolvo_sanuzlov'),
                ('otdelka', 'mebel'),
                ('bassein', 'zona_barbeku'),
            ),
        }),

    ]


admin.site.register(Dom, DomAdmin)