# Generated by Django 3.0.13 on 2021-06-02 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nedvizka_plugins', '0003_auto_20210602_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nedvizkafiltripoiskapluginpluginsetting',
            name='tip_nedvizki',
            field=models.CharField(choices=[('dom_prodaza', 'Дом-продажа'), ('dom_arenda', 'Дом-аренда'), ('kvartira_pervicka_prodaza', 'Квартира первичка - продажа'), ('kvartira_pervicka_arenda', 'Квартира первичка - аренда'), ('kvartira_vtoricka_prodaza', 'Квартира вторичка - продажа'), ('kvartira_vtoricka_arenda', 'Квартира вторичка - аренда'), ('kvartira_vtoricka_prodaza', 'Квартира вторичка - продажа'), ('kvartira_vtoricka_arenda', 'Квартира вторичка - аренда'), ('uchactki_prodaza', 'Участки - продажа'), ('uchactki_arenda', 'Участки - аренда'), ('nezilie_prodaza', 'Нежилые - продажа'), ('nezilie_arenda', 'Нежилые - аренда'), ('komerchiskie_prodaza', 'Комерчиские - продажа'), ('komerchiskie_arenda', 'Комерчиские - аренда')], max_length=255, verbose_name='Тип недвижки'),
        ),
        migrations.AlterField(
            model_name='nedvizkaspisokobiectovpluginpluginsetting',
            name='tip_nedvizki',
            field=models.CharField(choices=[('dom_prodaza', 'Дом-продажа'), ('dom_arenda', 'Дом-аренда'), ('kvartira_pervicka_prodaza', 'Квартира первичка - продажа'), ('kvartira_pervicka_arenda', 'Квартира первичка - аренда'), ('kvartira_vtoricka_prodaza', 'Квартира вторичка - продажа'), ('kvartira_vtoricka_arenda', 'Квартира вторичка - аренда'), ('kvartira_vtoricka_prodaza', 'Квартира вторичка - продажа'), ('kvartira_vtoricka_arenda', 'Квартира вторичка - аренда'), ('uchactki_prodaza', 'Участки - продажа'), ('uchactki_arenda', 'Участки - аренда'), ('nezilie_prodaza', 'Нежилые - продажа'), ('nezilie_arenda', 'Нежилые - аренда'), ('komerchiskie_prodaza', 'Комерчиские - продажа'), ('komerchiskie_arenda', 'Комерчиские - аренда')], max_length=255, verbose_name='Тип недвижки'),
        ),
    ]
