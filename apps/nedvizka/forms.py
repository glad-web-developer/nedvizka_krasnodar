from django import forms

from apps.nedvizka.CONST import CHOICES_NALICHIE_OTDELKI, CHOICES_DA_NET, CHOICES_NALICHIE_VNESNEI_OTDELKI
from apps.nedvizka.models import DomProdaza, TipMaloetaznoiPostroiki, MaterialMaoetaznoiPostroiki, TipKomerch, \
    TipNeziloe


class BaseSearch(forms.Form):
    nazvanie = forms.CharField(label='Название', required=False, )
    price_itogovaia_ot = forms.IntegerField(label='Цена от', required=False)
    price_itogovaia_do = forms.IntegerField(label='Цена до', required=False)
    obshaia_ploshad_ot = forms.IntegerField(label='Площадь от', required=False)
    obshaia_ploshad_do = forms.IntegerField(label='Площадь до', required=False)
    naselenii_punkt = forms.CharField(label='Населенный пункт', required=False)
    adres = forms.CharField(label='Адрес', required=False)


class MaloEtaznoeForm(forms.Form):
    nazvanie = forms.CharField(label='Название', required=False, )
    price_itogovaia_ot = forms.IntegerField(label='Цена от', required=False)
    price_itogovaia_do = forms.IntegerField(label='Цена до', required=False)
    obshaia_ploshad_ot = forms.IntegerField(label='Площадь от', required=False)
    obshaia_ploshad_do = forms.IntegerField(label='Площадь до', required=False)
    tip_maloetaznoi_postroiki = forms.ModelChoiceField(label='Тип постройки', required=False,
                                                       queryset=TipMaloetaznoiPostroiki.objects.all(), empty_label="---")
    material_postroiki = forms.ModelChoiceField(label='Материал постройки', required=False,
                                                       queryset=MaterialMaoetaznoiPostroiki.objects.all(), empty_label="---")


class DomProdazaForm(BaseSearch):
    nalichie_otdelki = forms.ChoiceField(label='Наличие внутренней отделки', choices=CHOICES_NALICHIE_OTDELKI,
                                         required=False)
    nalichie_gaza = forms.ChoiceField(label='Наличие газа', required=False, choices=CHOICES_DA_NET)
    blizost_so_shkoloi = forms.ChoiceField(label='Близость со школой/садиком', required=False, choices=CHOICES_DA_NET)
    blizost_s_med = forms.ChoiceField(label='Близость с мед учереждением', required=False, choices=CHOICES_DA_NET)
    blizost_s_metro = forms.ChoiceField(label='Близость с метро', required=False, choices=CHOICES_DA_NET)
    nalichie_vnesheni_otdelki = forms.ChoiceField(label='Наличие внешней отделки', required=False,
                                                  choices=CHOICES_NALICHIE_VNESNEI_OTDELKI)
    vodoprovod = forms.ChoiceField(label='Водопровод', required=False, choices=CHOICES_DA_NET)
    electrichestvo = forms.ChoiceField(label='Электричество', required=False, choices=CHOICES_DA_NET)
    ostanovki = forms.ChoiceField(label='Остановки', required=False, choices=CHOICES_DA_NET)


class KvartiraPervichkaProdazaForm(BaseSearch):
    nalichie_otdelki = forms.ChoiceField(label='Отделка', choices=CHOICES_NALICHIE_OTDELKI, required=False)
    nalichie_gaza = forms.ChoiceField(label='Наличие газа', required=False, choices=CHOICES_DA_NET)
    blizost_so_shkoloi = forms.ChoiceField(label='Близость со школой/садиком', required=False, choices=CHOICES_DA_NET)
    blizost_s_med = forms.ChoiceField(label='Близость с мед учереждением', required=False, choices=CHOICES_DA_NET)
    blizost_s_metro = forms.ChoiceField(label='Близость с метро', required=False, choices=CHOICES_DA_NET)
    ostanovki = forms.ChoiceField(label='Остановки', required=False, choices=CHOICES_DA_NET)


class KvartiraVtorichkaProdazaForm(BaseSearch):
    nalichie_otdelki = forms.ChoiceField(label='Отделка', choices=CHOICES_NALICHIE_OTDELKI, required=False)
    nalichie_gaza = forms.ChoiceField(label='Наличие газа', required=False, choices=CHOICES_DA_NET)
    blizost_so_shkoloi = forms.ChoiceField(label='Близость со школой/садиком', required=False, choices=CHOICES_DA_NET)
    blizost_s_med = forms.ChoiceField(label='Близость с мед учереждением', required=False, choices=CHOICES_DA_NET)
    blizost_s_metro = forms.ChoiceField(label='Близость с метро', required=False, choices=CHOICES_DA_NET)
    ostanovki = forms.ChoiceField(label='Остановки', required=False, choices=CHOICES_DA_NET)


class UchastkiProdazaForm(BaseSearch):
    vodoprovod = forms.ChoiceField(label='Водопровод', required=False, choices=CHOICES_DA_NET)
    electrichestvo = forms.ChoiceField(label='Электричество', required=False, choices=CHOICES_DA_NET)
    ostanovki = forms.ChoiceField(label='Остановки', required=False, choices=CHOICES_DA_NET)
    nalichie_gaza = forms.ChoiceField(label='Наличие газа', required=False, choices=CHOICES_DA_NET)



class NezelieProdazaForm(BaseSearch):
    tip_neziloe = forms.ModelChoiceField(label='Тип', required=False,
                                                       queryset=TipNeziloe.objects.all(), empty_label="---")


class KomerchiskieProdazaForm(BaseSearch):
    tip_komerch = forms.ModelChoiceField(label='Тип', required=False,
                                                       queryset=TipKomerch.objects.all(), empty_label="---")
