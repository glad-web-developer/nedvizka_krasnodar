# Generated by Django 3.0.13 on 2021-08-04 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nedvizka', '0020_auto_20210804_1031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='domprodaza',
            old_name='ploshad_ouchastka',
            new_name='ploshad_uchastka',
        ),
    ]
