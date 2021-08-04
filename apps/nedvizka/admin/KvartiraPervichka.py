from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.nedvizka.models import FotoKvartiraPervichkaProdaza,  KvartiraPervichkaProdaza


class FotoKvartiraPervichkaProdazaInline(admin.TabularInline):
    model = FotoKvartiraPervichkaProdaza
    extra = 0


class KvartiraPervichkaProdazaAdmin(ImportExportModelAdmin):
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
    inlines = [FotoKvartiraPervichkaProdazaInline, ]

    save_as = True
    save_on_top = True



admin.site.register(KvartiraPervichkaProdaza, KvartiraPervichkaProdazaAdmin)

