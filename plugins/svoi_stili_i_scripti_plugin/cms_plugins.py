from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from plugins.svoi_stili_i_scripti_plugin.models import SvoiStilIScriptPluginSetting


@plugin_pool.register_plugin
class SvoiStilIScriptPlugin(CMSPluginBase):

    render_template = "svoi_stili_i_scripti_plugin/lv.html"
    module = '01. Кастомные плагины'
    name = 'Стиль/Скрипт'
    model = SvoiStilIScriptPluginSetting

    allow_children = False

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context
