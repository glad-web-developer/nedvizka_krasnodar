from django.contrib import admin

from apps.nedvizka.models import FotoDomProdaza, VideoDomProdaza, PanoramiDomProdaza, DomProdaza, FotoDomArenda, \
    VideoDomArendda, PanoramiDomaArenda, DomArenda

from import_export.admin import ImportExportModelAdmin

from apps.nedvizka.models.MaloEtaznoeStroitelstvo import MaloEtaznoeStroitelstvoProdaza, TipMaloetaznoiPostroiki, \
    MaterialMaoetaznoiPostroiki, FotoMaloEtaznoeStroitelstvoProdaza


class FotoMaloEtaznoeStroitelstvoInline(admin.TabularInline):
    model = FotoMaloEtaznoeStroitelstvoProdaza
    extra = 4
    # classes = ['collapse']

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

    # fieldsets = [
    #     (None, {
    #         'fields': (
    #             'nazvanie',
    #             'slug',
    #             'previu',
    #             'pokazivat',
    #             'opisaanaie',
    #             ('price_bazovaia', 'prrice_akzionnaia', ),
    #             ('naselenii_punkt', 'adres'),
    #             ('obshaia_ploshad', 'ploshad_osnovnogo_doma'),
    #             ('nalichie_gaza', 'nalichie_otdelki', ),
    #             ('blizost_s_med', 'blizost_so_shkoloi', 'blizost_s_metro'),
    #         )
    #     }),
    # ]


admin.site.register(MaloEtaznoeStroitelstvoProdaza, MaloEtaznoeStroitelstvoProdazaAdmin)