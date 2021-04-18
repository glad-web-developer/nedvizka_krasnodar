# from cms.plugin_base import CMSPluginBase
# from cms.plugin_pool import plugin_pool
#
# from apps.novosti.models import Novost
# from math import ceil
#
#
# @plugin_pool.register_plugin
# class NovostiLvPlugin(CMSPluginBase):
#
#     render_template = "novosti/lv.html"
#     module = 'Плагины для Орешек'
#     name = 'Новости'
#     cache = False
#
#     def render(self, context, instance, placeholder):
#         page = 1
#         kol_vo_novostei = 6
#         try:
#             page = int(context['request'].GET['page'])
#         except Exception:
#             pass
#
#         novosti = Novost.objects.all()
#         novostei_vsego = len(novosti)
#         straniz_vsego = ceil(novostei_vsego / kol_vo_novostei)
#
#         if page > straniz_vsego:
#             page = 1
#
#         start = (page-1)*kol_vo_novostei
#         end = page*kol_vo_novostei
#
#         novosti = novosti[start:end]
#
#         context.update({'instance':instance, 'novosti':novosti, 'page_now':page, 'straniz_vsego':straniz_vsego})
#         return context
