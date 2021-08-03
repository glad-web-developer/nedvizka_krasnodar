# Generated by Django 3.0.13 on 2021-08-03 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nedvizka', '0018_auto_20210804_0231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domarenda',
            name='eto_luchoe_prodlozenie',
        ),
        migrations.RemoveField(
            model_name='domprodaza',
            name='eto_luchoe_prodlozenie',
        ),
        migrations.RemoveField(
            model_name='komerchiskiearenda',
            name='eto_luchoe_prodlozenie',
        ),
        migrations.RemoveField(
            model_name='komerchiskieprodaza',
            name='eto_luchoe_prodlozenie',
        ),
        migrations.RemoveField(
            model_name='kvartirapervichkaarenda',
            name='eto_luchoe_prodlozenie',
        ),
        migrations.RemoveField(
            model_name='kvartirapervichkaprodaza',
            name='eto_luchoe_prodlozenie',
        ),
        migrations.RemoveField(
            model_name='kvartiravtorichkaarenda',
            name='eto_luchoe_prodlozenie',
        ),
        migrations.RemoveField(
            model_name='kvartiravtorichkaprodaza',
            name='eto_luchoe_prodlozenie',
        ),
        migrations.RemoveField(
            model_name='nezeliearenda',
            name='eto_luchoe_prodlozenie',
        ),
        migrations.RemoveField(
            model_name='nezelieprodaza',
            name='eto_luchoe_prodlozenie',
        ),
        migrations.RemoveField(
            model_name='uchactkiarenda',
            name='eto_luchoe_prodlozenie',
        ),
        migrations.RemoveField(
            model_name='uchactkiprodaza',
            name='eto_luchoe_prodlozenie',
        ),
        migrations.AlterField(
            model_name='uchactkiprodaza',
            name='price_itogovaia',
            field=models.FloatField(default=0, editable=False, verbose_name='Цена для поиска'),
        ),
    ]
