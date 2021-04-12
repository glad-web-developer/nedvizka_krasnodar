from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from plugins.ssilka_navbar_plugin.models import SsilkaNavbarePluginSetting


@plugin_pool.register_plugin
class SsilkaNavbarePlugin(CMSPluginBase):

    render_template = "ssilka_navbar_plugin/lv.html"
    module = '01. Кастомные плагины'
    model = SsilkaNavbarePluginSetting
    name = 'Ссылка навбар'


    allow_children = False


    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

