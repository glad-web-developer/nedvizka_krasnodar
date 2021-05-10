# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals


from django.conf.urls import include, url

from plugins.formi_obratnoi_sviazi_plugin.views import otpravit_formu_zakaza_zvonka


app_name = 'formi_obratnoi_sviazi'
urlpatterns = (
    url(r'^', otpravit_formu_zakaza_zvonka, name='otpravit_formu_zakaza_zvonka'),
)