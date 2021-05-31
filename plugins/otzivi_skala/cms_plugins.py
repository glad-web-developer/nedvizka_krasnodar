from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from plugins.otzivi_skala.models import OtziviSkalaDvPluginSetting, OtziviSkalaLvPluginSetting


@plugin_pool.register_plugin
class OtziviSkalaLvPlugin(CMSPluginBase):

    render_template = "otzivi_skala/lv.html"
    module = '01. Кастомные плагины'
    model = OtziviSkalaLvPluginSetting
    name = 'Отзывы - слайдер тип 2'

    allow_children = True
    child_classes = ['OtziviSkalaDvPlugin', ]

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context


@plugin_pool.register_plugin
class OtziviSkalaDvPlugin(CMSPluginBase):

    render_template = "otzivi_skala/dv.html"
    module = '01. Кастомные плагины'
    model = OtziviSkalaDvPluginSetting
    name = 'Отзывы - слайдер тип 2'

    allow_children = False
    parent_classes = ['OtziviSkalaLvPlugin', ]

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context



