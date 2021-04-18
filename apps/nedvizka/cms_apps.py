# from cms.app_base import CMSApp
# from cms.apphook_pool import apphook_pool
# from django.conf.urls import url
#
# from apps.novosti.views import novosti_dv
#
# @apphook_pool.register
# class NovostiApp(CMSApp):
#     app_name = 'novosti'
#     name = "Новости"
#
#     def get_urls(self, page=None, language=None, **kwargs):
#         return [
#             # url(r'^$', uslugi_lv),
#             url(r'(?P<id>[-\w]+)/$', novosti_dv),
#         ]