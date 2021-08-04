from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from apps.nedvizka.models.MaloEtaznoeStroitelstvo import MaloEtaznoeStroitelstvoProdaza, TipMaloetaznoiPostroiki, \
    MaterialMaoetaznoiPostroiki, FotoMaloEtaznoeStroitelstvoProdaza


class FotoMaloEtaznoeStroitelstvoInline(admin.TabularInline):
    model = FotoMaloEtaznoeStroitelstvoProdaza
    extra = 0

class TipMaloetaznoiPostroikiAdmin(ImportExportModelAdmin):
    save_as = True
    save_on_top = True

admin.site.register(TipMaloetaznoiPostroiki, TipMaloetaznoiPostroikiAdmin)

class MaterialMaoetaznoiPostroikiAdmin(ImportExportModelAdmin):
    save_as = True
    save_on_top = True

admin.site.register(MaterialMaoetaznoiPostroiki, MaterialMaoetaznoiPostroikiAdmin)

class MaloEtaznoeStroitelstvoProdazaAdmin(ImportExportModelAdmin):
    list_display = [
        'id',
        'nazvanie',
        'tip_maloetaznoi_postroiki',
        'pokazivat',
        'price_bazovaia',
        'prrice_akzionnaia',
    ]
    search_fields = [
        'id',
        'nazvanie',
        'price_bazovaia',
        'prrice_akzionnaia',
    ]
    list_filter = [
        'pokazivat',
        'tip_maloetaznoi_postroiki',
    ]
    inlines = [FotoMaloEtaznoeStroitelstvoInline,]

    save_as = True
    save_on_top = True



admin.site.register(MaloEtaznoeStroitelstvoProdaza, MaloEtaznoeStroitelstvoProdazaAdmin)