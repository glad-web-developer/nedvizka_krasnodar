from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from plugins.price_list.models import PriceListLvPluginSetting, PriceListDvPluginSetting


@plugin_pool.register_plugin
class PriceListLvPlugin(CMSPluginBase):

    render_template = "price_list/lv.html"
    module = 'Кастомные плагины'
    model = PriceListLvPluginSetting
    name = 'Прайс - слайдер'

    allow_children = True
    child_classes = ['PriceListDvPlugin', ]

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context


@plugin_pool.register_plugin
class PriceListDvPlugin(CMSPluginBase):

    render_template = "price_list/dv.html"
    module = 'Кастомные плагины'
    model = PriceListDvPluginSetting
    name = 'Прайс - слайд'

    allow_children = False
    parent_classes = ['PriceListLvPlugin', ]

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context



