# Generated by Django 3.0.13 on 2021-05-30 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nedvizka', '0003_auto_20210530_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domprodaza',
            name='nomer',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Номер(id объекта)'),
        ),
    ]