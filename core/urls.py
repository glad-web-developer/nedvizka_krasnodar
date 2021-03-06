# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.shortcuts import render
from django.views.static import serve

from apps.nedvizka.views import api_ipoteka

admin.autodiscover()

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'cmspages': CMSSitemap}}),
]

def render_page_404(request):
    return render(request, 'core/page_templates/404.html')


urlpatterns += (
    url(r'^admin/', admin.site.urls),  # NOQA
    url(r'^formi_obratnoi_sviazi/', include('plugins.formi_obratnoi_sviazi_plugin.urls', namespace='formi_obratnoi_sviazi')),
    url(r'^api/ipoteka/', api_ipoteka),
    url(r'^error_404/', render_page_404),
    url(r'^', include('cms.urls')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns
