from django import forms

from apps.nedvizka.CONST import CHOICES_NALICHIE_OTDELKI
from apps.nedvizka.models import DomProdaza


class DomProdazaForm(forms.Form):
    nazvanie = forms.CharField(label='Название', required=False)
    price_itogovaia = forms.IntegerField(label='Цена', required=False)
    obshaia_ploshad = forms.CharField(label='Площадь', required=False)
    naselenii_punkt = forms.CharField(label='Населенный пункт', required=False)
    adres = forms.CharField(label='Адрес', required=False)

    nalichie_otdelki = forms.ChoiceField(label='Отделка', choices=CHOICES_NALICHIE_OTDELKI, required=False)
    nalichie_gaza = forms.BooleanField(label='Наличие газа', required=False)
    blizost_so_shkoloi = forms.BooleanField(label='Близость со школой', required=False)
    blizost_s_med = forms.BooleanField(label='Близость с мед учереждением', required=False)
    blizost_s_metro = forms.BooleanField(label='Близость с метро', required=False)
    page = forms.IntegerField(required=False, widget=forms.HiddenInput())
