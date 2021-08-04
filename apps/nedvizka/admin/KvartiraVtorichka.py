from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.nedvizka.models import FotoKvartiraVtorichkaProdaza, KvartiraVtorichkaProdaza


class FotoKvartiraVtorichkaProdazaInline(admin.TabularInline):
    model = FotoKvartiraVtorichkaProdaza
    extra = 0



class KvartiraVtorichkaProdazaAdmin(ImportExportModelAdmin):
    list_display = [
        'id',
        'nazvanie',
        'pokazivat',
        'price_bazovaia',
        'prrice_akzionnaia',
        'naselenii_punkt',
        'akzia'
    ]
    list_display_links =  [
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
    inlines = [FotoKvartiraVtorichkaProdazaInline, ]

    save_as = True
    save_on_top = True




admin.site.register(KvartiraVtorichkaProdaza, KvartiraVtorichkaProdazaAdmin)

