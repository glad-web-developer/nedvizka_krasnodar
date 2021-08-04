from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from apps.nedvizka.models import DomProdaza, KvartiraPervichkaProdaza, KvartiraVtorichkaProdaza, UchactkiProdaza, \
    NezelieProdaza, \
    KomerchiskieProdaza, MaloEtaznoeStroitelstvoProdaza


def dom_prodaza_dv(request, slug_or_id):
    try:
        danie_nedvizki = get_object_or_404(DomProdaza, slug=slug_or_id)
    except:
        danie_nedvizki = get_object_or_404(DomProdaza, id=slug_or_id)
    return render(request, 'nedvizka/straniza_dv_nedvizka.html', {'danie_nedvizki': danie_nedvizki})


def kvartira_pervichka_prodaza_dv(request, slug_or_id):
    try:
        danie_nedvizki = get_object_or_404(KvartiraPervichkaProdaza, slug=slug_or_id)
    except:
        danie_nedvizki = get_object_or_404(KvartiraPervichkaProdaza, id=slug_or_id)
    return render(request, 'nedvizka/straniza_dv_nedvizka.html', {'danie_nedvizki': danie_nedvizki})


# **************
def kvartira_vtorichka_prodaza_dv(request, slug_or_id):
    try:
        danie_nedvizki = get_object_or_404(KvartiraVtorichkaProdaza, slug=slug_or_id)
    except:
        danie_nedvizki = get_object_or_404(KvartiraVtorichkaProdaza, id=slug_or_id)
    return render(request, 'nedvizka/straniza_dv_nedvizka.html', {'danie_nedvizki': danie_nedvizki})


# **********

def uchactki_prodaza_dv(request, slug_or_id):
    try:
        danie_nedvizki = get_object_or_404(UchactkiProdaza, slug=slug_or_id)
    except:
        danie_nedvizki = get_object_or_404(UchactkiProdaza, id=slug_or_id)
    return render(request, 'nedvizka/straniza_dv_nedvizka.html', {'danie_nedvizki': danie_nedvizki})


# **********

def nezilie_prodaza_dv(request, slug_or_id):
    try:
        danie_nedvizki = get_object_or_404(NezelieProdaza, slug=slug_or_id)
    except:
        danie_nedvizki = get_object_or_404(NezelieProdaza, id=slug_or_id)
    return render(request, 'nedvizka/straniza_dv_nedvizka.html', {'danie_nedvizki': danie_nedvizki})


# **********

def komerchiskie_prodaza_dv(request, slug_or_id):
    try:
        danie_nedvizki = get_object_or_404(KomerchiskieProdaza, slug=slug_or_id)
    except:
        danie_nedvizki = get_object_or_404(KomerchiskieProdaza, id=slug_or_id)
    return render(request, 'nedvizka/straniza_dv_nedvizka.html', {'danie_nedvizki': danie_nedvizki})


def maloetaznoe_stroitelstvo_dv(request, slug_or_id):
    danie_nedvizki = get_object_or_404(MaloEtaznoeStroitelstvoProdaza, id=slug_or_id)
    return render(request, 'nedvizka/straniza_dv_nedvizka.html', {'danie_nedvizki': danie_nedvizki})


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def api_ipoteka(request):
    stoimost = 0
    ezemes_stavka = 0
    srok = 0
    stavka = 0
    pervonachalni_vznos = 0

    if request.GET.get('stoimost'):
        stoimost = int(request.GET.get('stoimost').replace(' ', '').replace(' ', ''))

    if request.GET.get('pervonachalni_vznos'):
        pervonachalni_vznos = int(request.GET.get('pervonachalni_vznos').replace(' ', '').replace(' ', ''))

    if request.GET.get('srok'):
        srok = int(request.GET.get('srok').replace(' ', '').replace(' ', ''))

    if request.GET.get('stavka'):
        stavka = float(request.GET.get('stavka').replace(',', '.').replace(' ', '').replace(' ', ''))

    summa_kredita = stoimost - pervonachalni_vznos
    ezemes_stavka = stavka / 12 / 100
    srok_ipoteki_mesiazev = 12 * srok
    obshiya_stavka = (1 + ezemes_stavka) ** srok_ipoteki_mesiazev
    ezemes_platez = summa_kredita * ezemes_stavka * obshiya_stavka / (obshiya_stavka - 1)
    pereplata = ezemes_platez * srok_ipoteki_mesiazev - summa_kredita
    obshaia_viplata = ezemes_platez * srok_ipoteki_mesiazev
    dolia_kredita = int(summa_kredita / obshaia_viplata * 100)
    dolia_pereplati = 100 - dolia_kredita

    if summa_kredita <= 0 or ezemes_platez <= 0:
        return JsonResponse({}, status=500)

    return JsonResponse({
        'summa_kredita': toFixed(summa_kredita),
        'ezemes_platez': toFixed(ezemes_platez),
        'pereplata': toFixed(pereplata),
        'obshaia_viplata': toFixed(obshaia_viplata),
        'dolia_kredita': dolia_kredita,
        'dolia_pereplati': dolia_pereplati,
    })
