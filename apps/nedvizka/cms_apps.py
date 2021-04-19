from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.conf.urls import url

from apps.nedvizka.views import dom_dv


@apphook_pool.register
class NovostiApp(CMSApp):
    app_name = 'nedvizka'
    name = "Недвижка"

    def get_urls(self, page=None, language=None, **kwargs):
        return [
            # url(r'^$', uslugi_lv),
            url(r'(?P<id>[-\w]+)/$', dom_dv, name='dom_dv'),
        ]