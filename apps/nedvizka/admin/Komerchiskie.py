from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.nedvizka.models import KomerchiskieProdaza, FotoKomerchiskieProdaza, TipKomerch

admin.site.register(TipKomerch)

class FotoKomerchiskieProdazaInline(admin.TabularInline):
    model = FotoKomerchiskieProdaza
    extra = 0

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

    list_display_links = [
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



admin.site.register(KomerchiskieProdaza, KomerchiskieProdazaAdmin)