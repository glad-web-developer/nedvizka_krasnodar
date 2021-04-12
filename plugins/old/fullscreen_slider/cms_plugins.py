from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from plugins.fullscreen_slider.models import FullscreenSliderLvPluginSetting, FullscreenSliderDvVideoPluginSetting


@plugin_pool.register_plugin
class FullscreenSliderLvPlugin(CMSPluginBase):

    render_template = "fullscreen_slider/lv.html"
    module = 'Кастомные плагины'
    model = FullscreenSliderLvPluginSetting
    name = 'Полноэкранный слайдер'

    allow_children = True
    child_classes = ['FullscreenSliderDvVideoPlugin', ]

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context


@plugin_pool.register_plugin
class FullscreenSliderDvVideoPlugin(CMSPluginBase):

    render_template = "fullscreen_slider/dv_video.html"
    module = 'Кастомные плагины'
    model = FullscreenSliderDvVideoPluginSetting
    name = 'Слайд видео'

    allow_children = False
    parent_classes = ['FullscreenSliderLvPlugin', ]

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context


