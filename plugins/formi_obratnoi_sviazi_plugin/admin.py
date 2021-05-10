from django.contrib import admin

from plugins.formi_obratnoi_sviazi_plugin.models import ZakazanieZvonki


class ZakazanieZvonkiAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'data', 'perezvonili']
    search_fields = ['id','phone',]
    list_filter  = ['data','perezvonili']
    list_editable = ['perezvonili',]

    save_as = True
    save_on_top = True

admin.site.register(ZakazanieZvonki, ZakazanieZvonkiAdmin)