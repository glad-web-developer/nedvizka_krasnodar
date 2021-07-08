from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse

from plugins.formi_obratnoi_sviazi_plugin.models import ZakazanieZvonki


def otpravit_formu_zakaza_zvonka(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        telo_pisma = f'Вас попросил(а) перезвонить {name} . Контакт {phone}'

        ZakazanieZvonki(name=name, phone=phone).save()
        send_mail('Вас просили перезвонить', telo_pisma, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER,])


        # send_mail('Вас попросили позвонить', telo_pisma, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'error'}, status=500)