from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool


from plugins.razmer_texta_plugin.models import RazmerTextaPluginSetting


@plugin_pool.register_plugin
class RazmerTextaPlugin(CMSPluginBase):

    render_template = "razmer_texta_plugin/lv.html"
    module = '01. Кастомные плагины'
    name = 'Размер текста'
    model = RazmerTextaPluginSetting


    allow_children = False
    text_enabled = True
    text_editor_preview = True


    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context
