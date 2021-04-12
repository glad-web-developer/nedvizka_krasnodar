from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from plugins.fullscreen_slider.models import FullscreenSliderLvPluginSetting, FullscreenSliderDvVideoPluginSetting
from plugins.pochemu_mi.models import PochemuMiLvPluginSetting, PochemuMiDvVideoPluginSetting


@plugin_pool.register_plugin
class PochemuMiLvPlugin(CMSPluginBase):

    render_template = "pochemu_mi/lv.html"
    module = 'Кастомные плагины'
    model = PochemuMiLvPluginSetting
    name = 'Почему мы - список'

    allow_children = True
    child_classes = ['PochemuMiDvPlugin', ]

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context


@plugin_pool.register_plugin
class PochemuMiDvPlugin(CMSPluginBase):

    render_template = "pochemu_mi/dv.html"
    module = 'Кастомные плагины'
    model = PochemuMiDvVideoPluginSetting
    name = 'Почему мы - ячейка'

    allow_children = False
    parent_classes = ['PochemuMiLvPlugin', ]

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context


