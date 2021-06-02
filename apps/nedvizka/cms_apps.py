from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.conf.urls import url
from django.urls import path

from apps.nedvizka.views import dom_prodaza_dv


@apphook_pool.register
class ProdazaDomovApp(CMSApp):
    app_name = 'prodaza_domov'
    name = "Продажа домов"

    def get_urls(self, page=None, language=None, **kwargs):
        return [
            path(r'<slug_or_id>/', dom_prodaza_dv),
        ]