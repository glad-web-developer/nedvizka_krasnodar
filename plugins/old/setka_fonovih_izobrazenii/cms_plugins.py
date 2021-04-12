from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from plugins.setka_fonovih_izobrazenii.models import SetkaFonovihIzobrazeniiLvSetting, SetkaFonovihIzobrazeniiDvSetting


@plugin_pool.register_plugin
class SetkaFonovihIzobrazeniiLvPlugin(CMSPluginBase):

    render_template = "setka_fonovih_izobrazenii/lv.html"
    module = 'Кастомные плагины'
    model = SetkaFonovihIzobrazeniiLvSetting
    name = 'Сетка фоновых изображений LV'

    allow_children = True
    child_classes = ['SetkaFonovihIzobrazeniiDvPlugin', ]

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context


@plugin_pool.register_plugin
class SetkaFonovihIzobrazeniiDvPlugin(CMSPluginBase):

    render_template = "setka_fonovih_izobrazenii/dv.html"
    module = 'Кастомные плагины'
    model = SetkaFonovihIzobrazeniiDvSetting
    name = 'Сетка фоновых изображений DV'

    allow_children = False
    parent_classes = ['SetkaFonovihIzobrazeniiLvPlugin', ]

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

