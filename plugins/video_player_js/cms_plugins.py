from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from plugins.video_player_js.models import VideoPlayerJSPluginSetting


@plugin_pool.register_plugin
class VideoPlayerJSPlugin(CMSPluginBase):

    render_template = "video_player_js/video_player_js.html"
    module = '01. Кастомные плагины'
    model = VideoPlayerJSPluginSetting
    name = 'Видео плеер JS'

    allow_children = False

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context



