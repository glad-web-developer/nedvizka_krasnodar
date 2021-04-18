# from django.contrib import admin
# from apps.novosti.models import  Novost, NovostImg
#
#
# class NovostImgInline(admin.TabularInline):
#     model = NovostImg
#     extra = 3
#     # fk_name = 'novost'
#
#
# class NovostAdmin(admin.ModelAdmin):
#     list_display = ['title','data_sozdania', 'anotazia']
#     search_fields = ['title',]
#     list_filter  = ['data_sozdania',]
#     inlines = [NovostImgInline,]
#
#     save_as = True
#     save_on_top = True
#
#
# admin.site.register(Novost, NovostAdmin)