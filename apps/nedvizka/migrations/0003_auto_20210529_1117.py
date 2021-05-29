# Generated by Django 3.0.13 on 2021-05-29 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nedvizka', '0002_auto_20210529_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='domprodaza',
            name='spalen',
            field=models.IntegerField(default=1, verbose_name='Спални (кол-во)'),
        ),
        migrations.AlterField(
            model_name='domprodaza',
            name='kordinati_na_karte',
            field=models.CharField(blank=True, help_text='Например "44.533249, 33.455248" без кавычек', max_length=255, null=True, verbose_name='Координаты на карте'),
        ),
    ]
