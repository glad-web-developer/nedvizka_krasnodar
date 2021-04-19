from django.core import serializers
from django.db.models.functions import Lower
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from apps.nedvizka.models import Dom


def dom_dv(request, id):
    danie_nedvizki = get_object_or_404(Dom, id=id)
    return render(request, 'nedvizka/straniza_dv_nedvizka.html', {'danie_nedvizki':danie_nedvizki})

