from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin

from plugins.foto_albom.models import FotoIzAlboma, FotoAlbomPluginSetting


class FotoInline(admin.TabularInline):
    model = FotoIzAlboma
    fk_name = 'fotoalbom'
    extra = 10


@plugin_pool.register_plugin
class FotoAlbomPlugin(CMSPluginBase):

    render_template = "foto_albom/lv.html"
    module = 'Кастомные плагины'
    name = 'Фотоальбом'
    model = FotoAlbomPluginSetting
    inlines = [FotoInline, ]

    allow_children = False
    # child_classes = ['FotoIzAlbomaPlugin', ]

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context
