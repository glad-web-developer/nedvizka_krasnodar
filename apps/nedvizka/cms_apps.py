from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.conf.urls import url
from django.urls import path

from apps.nedvizka.views import dom_prodaza_dv, kvartira_pervichka_prodaza_dv, dom_arenda_dv, kvartiri_arenda_dv


@apphook_pool.register
class ProdazaDomovApp(CMSApp):
    app_name = 'dom_prodaza'
    name = "Продажа домов"

    def get_urls(self, page=None, language=None, **kwargs):
        return [
            path(r'<slug_or_id>/', dom_prodaza_dv),
        ]

@apphook_pool.register
class ArendaDomovApp(CMSApp):
    app_name = 'dom_arenda'
    name = "Аренда домов"

    def get_urls(self, page=None, language=None, **kwargs):
        return [
            path(r'<slug_or_id>/', dom_arenda_dv),
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
class ArendaKvartirPervickaApp(CMSApp):
    app_name = 'kvartira_pervicka_arenda'
    name = "Аренда квартир первичка"

    def get_urls(self, page=None, language=None, **kwargs):
        return [
            path(r'<slug_or_id>/', kvartiri_arenda_dv),
        ]

# @apphook_pool.register
# class ProdazaKvartirVtorickaApp(CMSApp):
#     app_name = 'kvartira_vtoricka_prodaza'
#     name = "Продажа квартир вторичка"
#
#     def get_urls(self, page=None, language=None, **kwargs):
#         return [
#             path(r'<slug_or_id>/', dom_prodaza_dv),
#         ]
#
# @apphook_pool.register
# class ArendaKvartirVtorickaApp(CMSApp):
#     app_name = 'kvartira_vtoricka_arenda'
#     name = "Аренда квартир вторичка"
#
#     def get_urls(self, page=None, language=None, **kwargs):
#         return [
#             path(r'<slug_or_id>/', dom_prodaza_dv),
#         ]

# @apphook_pool.register
# class ProdazaUchactkiVtorickaApp(CMSApp):
#     app_name = 'uchactki_prodaza'
#     name = "Продажа участков"
#
#     def get_urls(self, page=None, language=None, **kwargs):
#         return [
#             path(r'<slug_or_id>/', dom_prodaza_dv),
#         ]
#
# @apphook_pool.register
# class ArendaUchactkiApp(CMSApp):
#     app_name = 'uchactki_arenda'
#     name = "Аренда участков"
#
#     def get_urls(self, page=None, language=None, **kwargs):
#         return [
#             path(r'<slug_or_id>/', dom_prodaza_dv),
#         ]


# @apphook_pool.register
# class ProdazaNezilieApp(CMSApp):
#     app_name = 'nezilie_prodaza'
#     name = "Продажа нежелых"
#
#     def get_urls(self, page=None, language=None, **kwargs):
#         return [
#             path(r'<slug_or_id>/', dom_prodaza_dv),
#         ]
#
# @apphook_pool.register
# class ArendaNezilieApp(CMSApp):
#     app_name = 'nezilie_arenda'
#     name = "Аренда нежелых"
#
#     def get_urls(self, page=None, language=None, **kwargs):
#         return [
#             path(r'<slug_or_id>/', dom_prodaza_dv),
#         ]

# @apphook_pool.register
# class ProdazaKomerchiskieApp(CMSApp):
#     app_name = 'komerchiskie_prodaza'
#     name = "Продажа комерчиских"
#
#     def get_urls(self, page=None, language=None, **kwargs):
#         return [
#             path(r'<slug_or_id>/', dom_prodaza_dv),
#         ]
#
# @apphook_pool.register
# class ArendaKomerchiskieApp(CMSApp):
#     app_name = 'komerchiskie_arenda'
#     name = "Аренда комерчиских"
#
#     def get_urls(self, page=None, language=None, **kwargs):
#         return [
#             path(r'<slug_or_id>/', dom_prodaza_dv),
#         ]