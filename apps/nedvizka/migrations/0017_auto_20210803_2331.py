# Generated by Django 3.0.13 on 2021-08-03 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nedvizka', '0016_auto_20210803_2327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maloetaznoestroitelstvoprodaza',
            old_name='ploshad_osnovnogo_doma',
            new_name='obshaia_ploshad',
        ),
    ]
