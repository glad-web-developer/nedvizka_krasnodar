# Generated by Django 3.0.13 on 2021-05-29 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nedvizka', '0003_auto_20210529_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domprodaza',
            name='spalen',
            field=models.IntegerField(blank=True, null=True, verbose_name='Спални (кол-во)'),
        ),
    ]
