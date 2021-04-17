from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin

from plugins.slaider_s_navigaziei_izobrazeniyami_plugin.models import SlaiderSNavigazieiIzobrazeniyamiPluginLvSetting, \
    SlaiderSNavigazieiIzobrazeniyami


class SlaidInline(admin.TabularInline):
    model = SlaiderSNavigazieiIzobrazeniyami
    fk_name = 'slaider'
    extra = 0



@plugin_pool.register_plugin
class SlaiderSNavigazieiIzobrazeniyamiLvPlugin(CMSPluginBase):

    render_template = "slaider_s_navigaziei_izobrazeniyami_plugin/lv.html"
    module = '01. Кастомные плагины'
    model = SlaiderSNavigazieiIzobrazeniyamiPluginLvSetting
    name = 'Слайдер с навигацией изображениями'

    inlines = [SlaidInline, ]

    allow_children = False

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

