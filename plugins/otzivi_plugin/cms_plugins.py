from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin


from plugins.otzivi_plugin.models import OtziviLvPluginSetting, OtzivDliaPlugina


class OtzivInline(admin.TabularInline):
    model = OtzivDliaPlugina
    fk_name = 'otziv_slaider'
    extra = 0

@plugin_pool.register_plugin
class OtziviLvPlugin(CMSPluginBase):

    render_template = "otzivi_plugin/lv.html"
    module = '01. Кастомные плагины'
    model = OtziviLvPluginSetting
    name = 'Отзывы - слайдер'

    inlines = [OtzivInline, ]

    allow_children = False





    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context
