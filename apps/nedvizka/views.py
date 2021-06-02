from django.core import serializers
from django.db.models.functions import Lower
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404

from apps.nedvizka.models import DomProdaza, KvartiraPervichkaProdaza, DomArenda, KvartiraPervichkaArenda


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

def kvartiri_arenda_dv(request, slug_or_id):
    try:
        danie_nedvizki = get_object_or_404(KvartiraPervichkaArenda, slug=slug_or_id)
    except:
        danie_nedvizki = get_object_or_404(KvartiraPervichkaArenda, id=slug_or_id)
    return render(request, 'nedvizka/straniza_dv_nedvizka.html', {'danie_nedvizki':danie_nedvizki})