from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.conf.urls import url
from django.urls import path

from apps.nedvizka.views import dom_prodaza_dv, kvartira_pervichka_prodaza_dv, \
    kvartira_vtorichka_prodaza_dv, uchactki_prodaza_dv, \
    nezilie_prodaza_dv, komerchiskie_prodaza_dv, \
    maloetaznoe_stroitelstvo_dv


@apphook_pool.register
class ProdazaDomovApp(CMSApp):
    app_name = 'dom_prodaza'
    name = "Продажа домов"

    def get_urls(self, page=None, language=None, **kwargs):
        return [
            path(r'<slug_or_id>/', dom_prodaza_dv),
        ]




@apphook_pool.register
class ProdazaKvartirPervickaApp(CMSApp):
    app_name = 'kvartira_pervicka_prodaza'
    name = "Продажа квартир первичка"

    def get_urls(self, page=None, language=None, **kwargs):
        return [
            path(r'<slug_or_id>/', kvartira_pervichka_prodaza_dv),
        ]



@apphook_pool.register
class ProdazaKvartirVtorickaApp(CMSApp):
    app_name = 'kvartira_vtoricka_prodaza'
    name = "Продажа квартир вторичка"

    def get_urls(self, page=None, language=None, **kwargs):
        return [
            path(r'<slug_or_id>/', kvartira_vtorichka_prodaza_dv),
        ]





@apphook_pool.register
class ProdazaUchactkiVtorickaApp(CMSApp):
    app_name = 'uchactki_prodaza'
    name = "Продажа участков"

    def get_urls(self, page=None, language=None, **kwargs):
        return [
            path(r'<slug_or_id>/', uchactki_prodaza_dv),
        ]



@apphook_pool.register
class ProdazaNezilieApp(CMSApp):
    app_name = 'nezilie_prodaza'
    name = "Продажа нежелых"

    def get_urls(self, page=None, language=None, **kwargs):
        return [
            path(r'<slug_or_id>/', nezilie_prodaza_dv),
        ]



@apphook_pool.register
class ProdazaKomerchiskieApp(CMSApp):
    app_name = 'komerchiskie_prodaza'
    name = "Продажа комерчиских"

    def get_urls(self, page=None, language=None, **kwargs):
        return [
            path(r'<slug_or_id>/', komerchiskie_prodaza_dv),
        ]


@apphook_pool.register
class MaloetaznoeStroitelstvoApp(CMSApp):
    app_name = 'maloetaznoe_sroitelstvo_app'
    name = "Малоэтажное строительство"

    def get_urls(self, page=None, language=None, **kwargs):
        return [
            path(r'<slug_or_id>/', maloetaznoe_stroitelstvo_dv),
        ]
