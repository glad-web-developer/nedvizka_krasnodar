from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from plugins.galereia.models import GalereiaLvNaGlavnoiPluginSetting



@plugin_pool.register_plugin
class GalereiaLvNaGlavnoiPlugin(CMSPluginBase):

    render_template = "galereia/lv_na_glavnoi.html"
    module = 'Кастомные плагины'
    model = GalereiaLvNaGlavnoiPluginSetting
    name = 'Галерея на главной'

    allow_children = False
    # child_classes = ['NapravleniaTrenirovokDvPlugin', ]

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

