from django.contrib import admin



from import_export.admin import ImportExportModelAdmin

from apps.nedvizka.models import FotoDomProdaza, DomProdaza


class FotoDomProdazaInline(admin.TabularInline):
    model = FotoDomProdaza
    extra = 0



class DomProdazaAdmin(ImportExportModelAdmin):
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
    inlines = [FotoDomProdazaInline,]

    save_as = True
    save_on_top = True




admin.site.register(DomProdaza, DomProdazaAdmin)
