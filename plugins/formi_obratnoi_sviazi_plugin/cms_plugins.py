from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from plugins.formi_obratnoi_sviazi_plugin.models import FormaObratnoiSviaziSetting


@plugin_pool.register_plugin
class FormaObratnoiSviaziSettingPlugin(CMSPluginBase):

    render_template = "formi_obratnoi_sviazi_plugin/lv.html"
    module = '01. Кастомные плагины'
    model = FormaObratnoiSviaziSetting
    name = 'Форма обратной связи'

    allow_children = False

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context



