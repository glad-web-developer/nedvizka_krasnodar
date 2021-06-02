from django import forms

from apps.nedvizka.CONST import CHOICES_NALICHIE_OTDELKI, CHOICES_DA_NET
from apps.nedvizka.models import DomProdaza


class DomProdazaForm(forms.Form):


    nazvanie = forms.CharField(label='Название', required=False, )
    price_itogovaia_ot = forms.IntegerField(label='Цена от', required=False)
    price_itogovaia_do = forms.IntegerField(label='Цена до', required=False)
    obshaia_ploshad_ot = forms.IntegerField(label='Площадь от', required=False)
    obshaia_ploshad_do = forms.IntegerField(label='Площадь до', required=False)
    naselenii_punkt = forms.CharField(label='Населенный пункт', required=False)
    adres = forms.CharField(label='Адрес', required=False)

    nalichie_otdelki = forms.ChoiceField(label='Отделка', choices=CHOICES_NALICHIE_OTDELKI, required=False)
    nalichie_gaza = forms.ChoiceField(label='Наличие газа', required=False, choices=CHOICES_DA_NET)
    blizost_so_shkoloi = forms.ChoiceField(label='Близость со школой', required=False, choices=CHOICES_DA_NET)
    blizost_s_med = forms.ChoiceField(label='Близость с мед учереждением', required=False, choices=CHOICES_DA_NET)
    blizost_s_metro = forms.ChoiceField(label='Близость с метро', required=False, choices=CHOICES_DA_NET)
