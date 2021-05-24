from math import ceil

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from apps.nedvizka.models import NedvizkaIzbranoePluginSetting, NedvizkaPanelUpravleniaPluginSetting, \
    NedvizkaSpisokObiectovPluginPluginSetting, Dom, NedvizkaFiltriPoiskaPluginPluginSetting


@plugin_pool.register_plugin
class NedvizkaSpisokObiectovPlugin(CMSPluginBase):

    render_template = "nedvizka/nedvizka_spisok_obiectov.html"
    module = '02. Недвижка'
    name = 'Список объектов'
    cache = False
    model = NedvizkaSpisokObiectovPluginPluginSetting


    def render(self, context, instance, placeholder):

        page = 1
        kol_vo_obiectov = instance.obiectov_na_stranize
        tip_nedvizki = instance.tip_nedvizki
        dannie_nedvizki = Dom.objects.select_related('previu').all()

        try:
            page = int(context['request'].GET['page'])
        except Exception:
            pass


        if tip_nedvizki == 'dom_prodaza':
            dannie_nedvizki = dannie_nedvizki.filter(tip_operazii=1)
        if tip_nedvizki == 'dom_arenda':
            dannie_nedvizki = dannie_nedvizki.filter(tip_operazii=2)

        dannie_nedvizki_vsego = len(dannie_nedvizki)
        straniz_vsego = ceil(dannie_nedvizki_vsego / kol_vo_obiectov)

        if page > straniz_vsego:
            page = 1

        start = (page - 1) * kol_vo_obiectov
        end = page * kol_vo_obiectov

        dannie_nedvizki = dannie_nedvizki[start:end]

        context.update({'instance': instance, 'dannie_nedvizki': dannie_nedvizki, 'page_now':page, 'straniz_vsego':straniz_vsego})
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

        context.update({'instance':instance})
        return context



@plugin_pool.register_plugin
class NedvizkaFiltriPoiskaPluginPlugin(CMSPluginBase):

    render_template = "nedvizka/nedvizka_filtri_plugin.html"
    module = '02. Недвижка'
    name = 'Фильтр и поиск'
    cache = False
    model = NedvizkaFiltriPoiskaPluginPluginSetting
#
    def render(self, context, instance, placeholder):

        context.update({'instance':instance})
        return context
