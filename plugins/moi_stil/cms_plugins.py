from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool


from plugins.moi_stil.models import MoiStilPluginSetting


@plugin_pool.register_plugin
class MoiStilPlugin(CMSPluginBase):

    render_template = "moi_stil/lv.html"
    module = '01. Кастомные плагины'
    name = 'Мой стиль'
    model = MoiStilPluginSetting


    allow_children = True



    def __str__(self):
        return '123'

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context
