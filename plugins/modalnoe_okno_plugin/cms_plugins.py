from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from plugins.modalnoe_okno_plugin.models import ModalnoeOknoPluginSetting


@plugin_pool.register_plugin
class ModalnoeOknoPlugin(CMSPluginBase):

    render_template = "modalnoe_okno_plugin/lv.html"
    module = '01. Кастомные плагины'
    model = ModalnoeOknoPluginSetting
    name = 'Модальное окно'

    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context



