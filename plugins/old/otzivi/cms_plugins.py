from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from plugins.otzivi.models import OtziviDvPluginSetting, OtziviLvPluginSetting


@plugin_pool.register_plugin
class OtziviLvPlugin(CMSPluginBase):

    render_template = "otzivi/lv.html"
    module = 'Кастомные плагины'
    model = OtziviLvPluginSetting
    name = 'Отзывы - слайдер'

    allow_children = True
    child_classes = ['OtziviDvPlugin', ]

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context


@plugin_pool.register_plugin
class OtziviDvPlugin(CMSPluginBase):

    render_template = "otzivi/dv.html"
    module = 'Кастомные плагины'
    model = OtziviDvPluginSetting
    name = 'Отзывы - слайд'

    allow_children = False
    parent_classes = ['OtziviLvPlugin', ]

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context



