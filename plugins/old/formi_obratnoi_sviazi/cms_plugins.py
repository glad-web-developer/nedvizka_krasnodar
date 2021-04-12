from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from plugins.formi_obratnoi_sviazi.models import FormaObratnoiSviaziSetting


@plugin_pool.register_plugin
class FormaObratnoiSviaziSettingPlugin(CMSPluginBase):

    render_template = "formi_obratnoi_sviazi/forma_obratnoi_sviazi.html"
    module = 'Кастомные плагины'
    model = FormaObratnoiSviaziSetting
    name = 'Форма обратной связи'

    allow_children = False

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context



