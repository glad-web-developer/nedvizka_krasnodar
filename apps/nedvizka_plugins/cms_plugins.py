from math import ceil

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from apps.nedvizka.forms import DomProdazaForm
from apps.nedvizka.models import DomProdaza, DomArenda
from apps.nedvizka_plugins.models import NedvizkaSpisokObiectovPluginPluginSetting, \
     NedvizkaFiltriPoiskaPluginPluginSetting


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
        dannie_nedvizki = []

        if tip_nedvizki =='dom_prodaza':
            dannie_nedvizki = DomProdaza.objects.select_related('previu').all()

        if tip_nedvizki =='dom_arenda':
            dannie_nedvizki = DomArenda.objects.select_related('previu').all()

        try:
            page = int(context['request'].GET['page'])
        except Exception:
            pass


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
class NedvizkaFiltriPoiskaPluginPlugin(CMSPluginBase):

    render_template = "nedvizka/nedvizka_filtri_plugin.html"
    module = '02. Недвижка'
    name = 'Фильтр и поиск'
    cache = False
    model = NedvizkaFiltriPoiskaPluginPluginSetting

    def render(self, context, instance, placeholder):
        form_url = ''
        form = []
        get_params = context['request'].GET
        if instance.tip_nedvizki == 'dom_prodaza':
            form = DomProdazaForm(get_params)
        context.update({'instance':instance, 'form_url':form_url, 'form':form})
        return context
