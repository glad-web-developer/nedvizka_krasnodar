from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from plugins.trenera.models import TreneraLvSetting, TreneraDvSetting


@plugin_pool.register_plugin
class TreneraLvPlugin(CMSPluginBase):

    render_template = "trenera/lv.html"
    module = 'Кастомные плагины'
    model = TreneraLvSetting
    name = 'Список тренеров'

    allow_children = True
    child_classes = ['TreneraDvPlugin', ]

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context


@plugin_pool.register_plugin
class TreneraDvPlugin(CMSPluginBase):

    render_template = "trenera/dv.html"
    module = 'Кастомные плагины'
    model = TreneraDvSetting
    name = 'Тренер'

    allow_children = False
    parent_classes = ['TreneraLvPlugin', ]

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

