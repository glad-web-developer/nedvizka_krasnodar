from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from apps.nedvizka.models import NedvizkaIzbranoePluginSetting, NedvizkaPanelUpravleniaPluginSetting, \
    NedvizkaSpisokObiectovPluginPluginSetting, Dom


@plugin_pool.register_plugin
class NedvizkaSpisokObiectovPlugin(CMSPluginBase):

    render_template = "nedvizka/nedvizka_spisok_obiectov.html"
    module = '02. Недвижка'
    name = 'Список объектов'
    cache = False
    model = NedvizkaSpisokObiectovPluginPluginSetting

    def render(self, context, instance, placeholder):
        tip_nedvizki = instance.tip_nedvizki

        dannie_nedvizki = []
        if tip_nedvizki == 'dom_prodaza':
            dannie_nedvizki = Dom.objects.filter(tip_operazii=1)
        if tip_nedvizki == 'dom_arenda':
            dannie_nedvizki = Dom.objects.filter(tip_operazii=2)

        context.update({'instance': instance, 'dannie_nedvizki': dannie_nedvizki})
        return context

@plugin_pool.register_plugin
class NedvizkaPanelUpravleniaPlugin(CMSPluginBase):

    render_template = "nedvizka/nedvizka_panel_upravlenia.html"
    module = '02. Недвижка'
    name = 'Панель управления(карта+сортировка)'
    cache = False
    model = NedvizkaPanelUpravleniaPluginSetting

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context




@plugin_pool.register_plugin
class NedvizkaIzbranoePlugin(CMSPluginBase):

    render_template = "nedvizka/nedvizka_izbranoe_plugin.html"
    module = '02. Недвижка'
    name = 'Избранное'
    cache = False
    model = NedvizkaIzbranoePluginSetting
#
    def render(self, context, instance, placeholder):
        # page = 1
        # kol_vo_novostei = 6
        # try:
        #     page = int(context['request'].GET['page'])
        # except Exception:
        #     pass
        # 
        # novosti = Novost.objects.all()
        # novostei_vsego = len(novosti)
        # straniz_vsego = ceil(novostei_vsego / kol_vo_novostei)
        # 
        # if page > straniz_vsego:
        #     page = 1
        # 
        # start = (page-1)*kol_vo_novostei
        # end = page*kol_vo_novostei
        # 
        # novosti = novosti[start:end]

        # context.update({'instance':instance, 'novosti':novosti, 'page_now':page, 'straniz_vsego':straniz_vsego})
        context.update({'instance':instance})
        return context
