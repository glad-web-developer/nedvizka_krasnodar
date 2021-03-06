from math import ceil

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from apps.nedvizka.forms import DomProdazaForm, KvartiraPervichkaProdazaForm, \
    KvartiraVtorichkaProdazaForm, UchastkiProdazaForm, \
    NezelieProdazaForm, KomerchiskieProdazaForm, MaloEtaznoeForm
from apps.nedvizka.models import DomProdaza, KvartiraPervichkaProdaza, \
    KvartiraVtorichkaProdaza, UchactkiProdaza, NezelieProdaza, \
    KomerchiskieProdaza, MaloEtaznoeStroitelstvoProdaza, Doma
from apps.nedvizka_plugins.models import NedvizkaSpisokObiectovPluginPluginSetting, \
    NedvizkaFiltriPoiskaPluginPluginSetting


@plugin_pool.register_plugin
class NedvizkaSpisokObiectovPlugin(CMSPluginBase):
    render_template = "nedvizka/nedvizka_spisok_obiectov.html"
    module = '02. Недвижка'
    name = 'Список объектов'
    cache = False
    model = NedvizkaSpisokObiectovPluginPluginSetting

    def filtrazia_po_bazovim_poliam(self, dannie_nedvizki, params_poiska):
        if 'nazvanie' in params_poiska:
            if params_poiska['nazvanie']:
                dannie_nedvizki = dannie_nedvizki.filter(nazvanie__icontains=params_poiska['nazvanie'])
        if 'price_itogovaia_ot' in params_poiska:
            if params_poiska['price_itogovaia_ot']:
                dannie_nedvizki = dannie_nedvizki.filter(price_itogovaia__gte=params_poiska['price_itogovaia_ot'])
        if 'price_itogovaia_do' in params_poiska:
            if params_poiska['price_itogovaia_do']:
                dannie_nedvizki = dannie_nedvizki.filter(price_itogovaia__lte=params_poiska['price_itogovaia_do'])
        if 'obshaia_ploshad_ot' in params_poiska:
            if params_poiska['obshaia_ploshad_ot']:
                dannie_nedvizki = dannie_nedvizki.filter(obshaia_ploshad__gte=params_poiska['obshaia_ploshad_ot'])
        if 'obshaia_ploshad_do' in params_poiska:
            if params_poiska['obshaia_ploshad_do']:
                dannie_nedvizki = dannie_nedvizki.filter(obshaia_ploshad__lte=params_poiska['obshaia_ploshad_do'])
        if 'naselenii_punkt' in params_poiska:
            if params_poiska['naselenii_punkt']:
                dannie_nedvizki = dannie_nedvizki.filter(naselenii_punkt__icontains=params_poiska['naselenii_punkt'])

        if 'nalichie_vnesheni_otdelki' in params_poiska:
            if params_poiska['nalichie_vnesheni_otdelki']:
                dannie_nedvizki = dannie_nedvizki.filter(
                    nalichie_vnesheni_otdelki=params_poiska['nalichie_vnesheni_otdelki'])

        if 'vodoprovod' in params_poiska:
            if params_poiska['vodoprovod']:
                dannie_nedvizki = dannie_nedvizki.filter(vodoprovod=params_poiska['vodoprovod'])

        if 'electrichestvo' in params_poiska:
            if params_poiska['electrichestvo']:
                dannie_nedvizki = dannie_nedvizki.filter(vodoprovod=params_poiska['electrichestvo'])

        if 'ostanovki' in params_poiska:
            if params_poiska['ostanovki']:
                tmp = not params_poiska['ostanovki']
                dannie_nedvizki = dannie_nedvizki.filter(ostanovki__isnull=tmp)

        if 'adres' in params_poiska:
            if params_poiska['adres']:
                dannie_nedvizki = dannie_nedvizki.filter(adres__icontains=params_poiska['adres'])
        if 'nalichie_otdelki' in params_poiska:
            if params_poiska['nalichie_otdelki']:
                dannie_nedvizki = dannie_nedvizki.filter(nalichie_otdelki=params_poiska['nalichie_otdelki'])
        if 'nalichie_gaza' in params_poiska:
            if params_poiska['nalichie_gaza']:
                dannie_nedvizki = dannie_nedvizki.filter(nalichie_gaza=params_poiska['nalichie_gaza'])
        if 'blizost_so_shkoloi' in params_poiska:
            if params_poiska['blizost_so_shkoloi']:
                dannie_nedvizki = dannie_nedvizki.filter(blizost_so_shkoloi=params_poiska['blizost_so_shkoloi'])
        if 'blizost_s_med' in params_poiska:
            if params_poiska['blizost_s_med']:
                dannie_nedvizki = dannie_nedvizki.filter(blizost_s_med=params_poiska['blizost_s_med'])
        if 'blizost_s_metro' in params_poiska:
            if params_poiska['blizost_s_metro']:
                dannie_nedvizki = dannie_nedvizki.filter(blizost_s_metro=params_poiska['blizost_s_metro'])

        if 'tip_komerch' in params_poiska:
            if params_poiska['tip_komerch']:
                dannie_nedvizki = dannie_nedvizki.filter(tip_komerch=params_poiska['tip_komerch'])

        if 'tip_neziloe' in params_poiska:
            if params_poiska['tip_neziloe']:
                dannie_nedvizki = dannie_nedvizki.filter(tip_neziloe=params_poiska['tip_neziloe'])


        if 'material_postroiki' in params_poiska:
            if params_poiska['material_postroiki']:
                dannie_nedvizki = dannie_nedvizki.filter(material_postroiki_id=params_poiska['material_postroiki'])
        if 'tip_maloetaznoi_postroiki' in params_poiska:
            if params_poiska['tip_maloetaznoi_postroiki']:
                dannie_nedvizki = dannie_nedvizki.filter(tip_maloetaznoi_postroiki_id=params_poiska['tip_maloetaznoi_postroiki'])

        return dannie_nedvizki

    def render(self, context, instance, placeholder):

        page = 1
        dannie_nedvizki = []
        kol_vo_obiectov = instance.obiectov_na_stranize
        tip_nedvizki = instance.tip_nedvizki

        if tip_nedvizki == 'dom_prodaza':
            dannie_nedvizki = DomProdaza.objects.select_related('previu').all()


        if tip_nedvizki == 'kvartira_pervicka_prodaza':
            dannie_nedvizki = KvartiraPervichkaProdaza.objects.select_related('previu').all()



        if tip_nedvizki == 'kvartira_vtoricka_prodaza':
            dannie_nedvizki = KvartiraVtorichkaProdaza.objects.select_related('previu').all()


        if tip_nedvizki == 'uchactki_prodaza':
            dannie_nedvizki = UchactkiProdaza.objects.select_related('previu').all()



        if tip_nedvizki == 'nezilie_prodaza':
            dannie_nedvizki = NezelieProdaza.objects.select_related('previu').all()


        if tip_nedvizki == 'komerchiskie_prodaza':
            dannie_nedvizki = KomerchiskieProdaza.objects.select_related('previu').all()


        if tip_nedvizki == 'maloetaznoe_stroitelstvo':
            dannie_nedvizki = MaloEtaznoeStroitelstvoProdaza.objects.select_related('previu').all()

        params_poiska = context['request'].GET
        dannie_nedvizki = dannie_nedvizki.filter(pokazivat=True)
        dannie_nedvizki = self.filtrazia_po_bazovim_poliam(dannie_nedvizki, params_poiska)

        try:
            page = int(params_poiska['page'])
        except Exception:
            pass

        dannie_nedvizki_vsego = len(dannie_nedvizki)
        straniz_vsego = ceil(dannie_nedvizki_vsego / kol_vo_obiectov)

        if page > straniz_vsego:
            page = 1

        start = (page - 1) * kol_vo_obiectov
        end = page * kol_vo_obiectov

        dannie_nedvizki = dannie_nedvizki[start:end]
        naideno_zapisei = len(dannie_nedvizki)

        context.update(
            {'instance': instance, 'dannie_nedvizki': dannie_nedvizki, 'page_now': page, 'straniz_vsego': straniz_vsego,
             'naideno_zapisei': naideno_zapisei, 'dannie_nedvizki_vsego': dannie_nedvizki_vsego, 'start': start + 1,
             'end': start + naideno_zapisei})
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
        params = context['request'].GET

        if instance.tip_nedvizki == 'dom_prodaza':
            form = DomProdazaForm(params)

        if instance.tip_nedvizki == 'maloetaznoe_stroitelstvo':
            form = MaloEtaznoeForm(params)


        if instance.tip_nedvizki == 'kvartira_pervicka_prodaza':
            form = KvartiraPervichkaProdazaForm(params)


        if instance.tip_nedvizki == 'kvartira_vtoricka_prodaza':
            form = KvartiraVtorichkaProdazaForm(params)


        if instance.tip_nedvizki == 'uchactki_prodaza':
            form = UchastkiProdazaForm(params)


        if instance.tip_nedvizki == 'nezilie_prodaza':
            form = NezelieProdazaForm(params)


        if instance.tip_nedvizki == 'komerchiskie_prodaza':
            form = KomerchiskieProdazaForm(params)


        context.update({'instance': instance, 'form_url': form_url, 'form': form})
        return context
