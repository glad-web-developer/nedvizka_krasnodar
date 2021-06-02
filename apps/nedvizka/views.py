from django.core import serializers
from django.db.models.functions import Lower
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404

from apps.nedvizka.models import DomProdaza, KvartiraPervichkaProdaza, DomArenda, KvartiraPervichkaArenda, \
    KvartiraVtorichkaProdaza, KvartiraVtorichkaArenda, UchactkiProdaza, UchactkiArenda, NezelieArenda, NezelieProdaza, \
    KomerchiskieProdaza, KomerchiskieArenda


def dom_prodaza_dv(request, slug_or_id):
    try:
        danie_nedvizki = get_object_or_404(DomProdaza, slug=slug_or_id)
    except:
        danie_nedvizki = get_object_or_404(DomProdaza, id=slug_or_id)
    return render(request, 'nedvizka/straniza_dv_nedvizka.html', {'danie_nedvizki':danie_nedvizki})


def dom_arenda_dv(request, slug_or_id):
    try:
        danie_nedvizki = get_object_or_404(DomArenda, slug=slug_or_id)
    except:
        danie_nedvizki = get_object_or_404(DomArenda, id=slug_or_id)
    return render(request, 'nedvizka/straniza_dv_nedvizka.html', {'danie_nedvizki':danie_nedvizki})


def kvartira_pervichka_prodaza_dv(request, slug_or_id):
    try:
        danie_nedvizki = get_object_or_404(KvartiraPervichkaProdaza, slug=slug_or_id)
    except:
        danie_nedvizki = get_object_or_404(KvartiraPervichkaProdaza, id=slug_or_id)
    return render(request, 'nedvizka/straniza_dv_nedvizka.html', {'danie_nedvizki':danie_nedvizki})

def kvartiri_pervicka_arenda_dv(request, slug_or_id):
    try:
        danie_nedvizki = get_object_or_404(KvartiraPervichkaArenda, slug=slug_or_id)
    except:
        danie_nedvizki = get_object_or_404(KvartiraPervichkaArenda, id=slug_or_id)
    return render(request, 'nedvizka/straniza_dv_nedvizka.html', {'danie_nedvizki':danie_nedvizki})


# **************
def kvartira_vtorichka_prodaza_dv(request, slug_or_id):
    try:
        danie_nedvizki = get_object_or_404(KvartiraVtorichkaProdaza, slug=slug_or_id)
    except:
        danie_nedvizki = get_object_or_404(KvartiraVtorichkaProdaza, id=slug_or_id)
    return render(request, 'nedvizka/straniza_dv_nedvizka.html', {'danie_nedvizki':danie_nedvizki})

def kvartiri_vtorichka_arenda_dv(request, slug_or_id):
    try:
        danie_nedvizki = get_object_or_404(KvartiraVtorichkaArenda, slug=slug_or_id)
    except:
        danie_nedvizki = get_object_or_404(KvartiraVtorichkaArenda, id=slug_or_id)
    return render(request, 'nedvizka/straniza_dv_nedvizka.html', {'danie_nedvizki':danie_nedvizki})

# **********

def uchactki_prodaza_dv(request, slug_or_id):
    try:
        danie_nedvizki = get_object_or_404(UchactkiProdaza, slug=slug_or_id)
    except:
        danie_nedvizki = get_object_or_404(UchactkiProdaza, id=slug_or_id)
    return render(request, 'nedvizka/straniza_dv_nedvizka.html', {'danie_nedvizki':danie_nedvizki})

def uchactki_arenda_dv(request, slug_or_id):
    try:
        danie_nedvizki = get_object_or_404(UchactkiArenda, slug=slug_or_id)
    except:
        danie_nedvizki = get_object_or_404(UchactkiArenda, id=slug_or_id)
    return render(request, 'nedvizka/straniza_dv_nedvizka.html', {'danie_nedvizki':danie_nedvizki})

# **********

def nezilie_prodaza_dv(request, slug_or_id):
    try:
        danie_nedvizki = get_object_or_404(NezelieProdaza, slug=slug_or_id)
    except:
        danie_nedvizki = get_object_or_404(NezelieProdaza, id=slug_or_id)
    return render(request, 'nedvizka/straniza_dv_nedvizka.html', {'danie_nedvizki':danie_nedvizki})

def nezilie_arenda_dv(request, slug_or_id):
    try:
        danie_nedvizki = get_object_or_404(NezelieArenda, slug=slug_or_id)
    except:
        danie_nedvizki = get_object_or_404(NezelieArenda, id=slug_or_id)
    return render(request, 'nedvizka/straniza_dv_nedvizka.html', {'danie_nedvizki':danie_nedvizki})

# **********

def komerchiskie_prodaza_dv(request, slug_or_id):
    try:
        danie_nedvizki = get_object_or_404(KomerchiskieProdaza, slug=slug_or_id)
    except:
        danie_nedvizki = get_object_or_404(KomerchiskieProdaza, id=slug_or_id)
    return render(request, 'nedvizka/straniza_dv_nedvizka.html', {'danie_nedvizki':danie_nedvizki})

def komerchiskie_arenda_dv(request, slug_or_id):
    try:
        danie_nedvizki = get_object_or_404(KomerchiskieArenda, slug=slug_or_id)
    except:
        danie_nedvizki = get_object_or_404(KomerchiskieArenda, id=slug_or_id)
    return render(request, 'nedvizka/straniza_dv_nedvizka.html', {'danie_nedvizki':danie_nedvizki})