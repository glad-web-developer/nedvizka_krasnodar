from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.nedvizka.models import UchactkiProdaza, FotoUchactkiProdaza


class FotoUchactkiProdazaInline(admin.TabularInline):
    model = FotoUchactkiProdaza
    extra = 0


class UchactkiProdazaAdmin(ImportExportModelAdmin):
    list_display = [
        'id',
        'nazvanie',
        'pokazivat',
        'price_bazovaia',
        'prrice_akzionnaia',
        'naselenii_punkt',
        'akzia'
    ]
    list_display_links = [
        'id',
        'nazvanie',
        'pokazivat',
        'price_bazovaia',
        'prrice_akzionnaia',
        'naselenii_punkt',
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


admin.site.register(UchactkiProdaza, UchactkiProdazaAdmin)
