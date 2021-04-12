from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from plugins.fonovoe_izobrazenie_plugin.models import FonovoeIzobrazeniePluginSetting


@plugin_pool.register_plugin
class FonovoeIzobrazeniePlugin(CMSPluginBase):

    render_template = "fonovoe_izobrazenie_plugin/lv.html"
    module = '01. Кастомные плагины'
    model = FonovoeIzobrazeniePluginSetting
    name = 'Фоновое изображение'


    # fieldsets = [
    #     (None, {
    #         'fields': (
    #             'card_type',
    #             ('card_context', 'card_text_color'),
    #             ('card_alignment', 'card_outline'),
    #         )
    #     }),
    #     ('Advanced settings'), {
    #         'classes': ('collapse',),
    #         'fields': (
    #             'tag_type',
    #             'attributes',
    #         )
    #     },
    # ]

    allow_children = True
    # child_classes = ['FullscreenSliderDvVideoPlugin', ]

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

