from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from plugins.stilizovani_zagolovok_plugin.models import StilizovaniZagolovokPluginSetting


@plugin_pool.register_plugin
class StilizovaniZagolovokPlugin(CMSPluginBase):
    render_template = "stilizovani_zagolovok_plugin/lv.html"
    module = '01. Кастомные плагины'
    name = 'Стилизованный заголовок'
    model = StilizovaniZagolovokPluginSetting

    allow_children = False

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context
