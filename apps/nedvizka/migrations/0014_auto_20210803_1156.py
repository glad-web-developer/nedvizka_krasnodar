# Generated by Django 3.0.13 on 2021-08-03 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nedvizka', '0013_auto_20210602_1444'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PanoramiArenda',
            new_name='PanoramiDomaArenda',
        ),
        migrations.AlterModelOptions(
            name='komerchiskiearenda',
            options={'verbose_name': 'Комерчиские - аренда', 'verbose_name_plural': 'Комерчиские - аренда'},
        ),
        migrations.AlterModelOptions(
            name='komerchiskieprodaza',
            options={'verbose_name': 'Комерчиские - продажа', 'verbose_name_plural': 'Комерчиские - продажа'},
        ),
        migrations.AlterModelOptions(
            name='kvartiravtorichkaarenda',
            options={'verbose_name': 'Квартиры вторичка - аренда', 'verbose_name_plural': 'Квартиры вторичка - аренда'},
        ),
        migrations.AlterModelOptions(
            name='kvartiravtorichkaprodaza',
            options={'verbose_name': 'Квартира вторичка - продажа', 'verbose_name_plural': 'Квартира вторичка - продажа'},
        ),
        migrations.AlterModelOptions(
            name='nezeliearenda',
            options={'verbose_name': 'Нежилые - аренда', 'verbose_name_plural': 'Нежилые - аренда'},
        ),
        migrations.AlterModelOptions(
            name='nezelieprodaza',
            options={'verbose_name': 'Нежилые - продажа', 'verbose_name_plural': 'Нежилые - продажа'},
        ),
        migrations.AlterModelOptions(
            name='uchactkiarenda',
            options={'verbose_name': 'Участки - аренда', 'verbose_name_plural': 'Участки - аренда'},
        ),
        migrations.AlterModelOptions(
            name='uchactkiprodaza',
            options={'verbose_name': 'Участки - продажа', 'verbose_name_plural': 'Участки - продажа'},
        ),
        migrations.AlterField(
            model_name='domarenda',
            name='akzia',
            field=models.BooleanField(default=False, editable=False, verbose_name='Акция/спец цена'),
        ),
        migrations.AlterField(
            model_name='domarenda',
            name='blizost_s_med',
            field=models.BooleanField(choices=[(None, '---'), (True, 'Да'), (False, 'Нет')], default=False, verbose_name='Близость с мед учереждением'),
        ),
        migrations.AlterField(
            model_name='domarenda',
            name='blizost_s_metro',
            field=models.BooleanField(choices=[(None, '---'), (True, 'Да'), (False, 'Нет')], default=False, verbose_name='Близость с метро'),
        ),
        migrations.AlterField(
            model_name='domarenda',
            name='blizost_so_shkoloi',
            field=models.BooleanField(choices=[(None, '---'), (True, 'Да'), (False, 'Нет')], default=False, verbose_name='Близость со школой'),
        ),
        migrations.AlterField(
            model_name='domarenda',
            name='nalichie_gaza',
            field=models.BooleanField(choices=[(None, '---'), (True, 'Да'), (False, 'Нет')], default=False, verbose_name='Наличие газа в доме'),
        ),
        migrations.AlterField(
            model_name='domprodaza',
            name='akzia',
            field=models.BooleanField(default=False, editable=False, verbose_name='Акция/спец цена'),
        ),
        migrations.AlterField(
            model_name='komerchiskiearenda',
            name='akzia',
            field=models.BooleanField(default=False, editable=False, verbose_name='Акция/спец цена'),
        ),
        migrations.AlterField(
            model_name='komerchiskiearenda',
            name='blizost_s_med',
            field=models.BooleanField(choices=[(None, '---'), (True, 'Да'), (False, 'Нет')], default=False, verbose_name='Близость с мед учереждением'),
        ),
        migrations.AlterField(
            model_name='komerchiskiearenda',
            name='blizost_s_metro',
            field=models.BooleanField(choices=[(None, '---'), (True, 'Да'), (False, 'Нет')], default=False, verbose_name='Близость с метро'),
        ),
        migrations.AlterField(
            model_name='komerchiskiearenda',
            name='blizost_so_shkoloi',
            field=models.BooleanField(choices=[(None, '---'), (True, 'Да'), (False, 'Нет')], default=False, verbose_name='Близость со школой'),
        ),
        migrations.AlterField(
            model_name='komerchiskiearenda',
            name='nalichie_gaza',
            field=models.BooleanField(choices=[(None, '---'), (True, 'Да'), (False, 'Нет')], default=False, verbose_name='Наличие газа в доме'),
        ),
        migrations.AlterField(
            model_name='komerchiskieprodaza',
            name='akzia',
            field=models.BooleanField(default=False, editable=False, verbose_name='Акция/спец цена'),
        ),
        migrations.AlterField(
            model_name='kvartirapervichkaarenda',
            name='akzia',
            field=models.BooleanField(default=False, editable=False, verbose_name='Акция/спец цена'),
        ),
        migrations.AlterField(
            model_name='kvartirapervichkaarenda',
            name='blizost_s_med',
            field=models.BooleanField(choices=[(None, '---'), (True, 'Да'), (False, 'Нет')], default=False, verbose_name='Близость с мед учереждением'),
        ),
        migrations.AlterField(
            model_name='kvartirapervichkaarenda',
            name='blizost_s_metro',
            field=models.BooleanField(choices=[(None, '---'), (True, 'Да'), (False, 'Нет')], default=False, verbose_name='Близость с метро'),
        ),
        migrations.AlterField(
            model_name='kvartirapervichkaarenda',
            name='blizost_so_shkoloi',
            field=models.BooleanField(choices=[(None, '---'), (True, 'Да'), (False, 'Нет')], default=False, verbose_name='Близость со школой'),
        ),
        migrations.AlterField(
            model_name='kvartirapervichkaarenda',
            name='nalichie_gaza',
            field=models.BooleanField(choices=[(None, '---'), (True, 'Да'), (False, 'Нет')], default=False, verbose_name='Наличие газа в доме'),
        ),
        migrations.AlterField(
            model_name='kvartirapervichkaprodaza',
            name='akzia',
            field=models.BooleanField(default=False, editable=False, verbose_name='Акция/спец цена'),
        ),
        migrations.AlterField(
            model_name='kvartiravtorichkaarenda',
            name='akzia',
            field=models.BooleanField(default=False, editable=False, verbose_name='Акция/спец цена'),
        ),
        migrations.AlterField(
            model_name='kvartiravtorichkaarenda',
            name='blizost_s_med',
            field=models.BooleanField(choices=[(None, '---'), (True, 'Да'), (False, 'Нет')], default=False, verbose_name='Близость с мед учереждением'),
        ),
        migrations.AlterField(
            model_name='kvartiravtorichkaarenda',
            name='blizost_s_metro',
            field=models.BooleanField(choices=[(None, '---'), (True, 'Да'), (False, 'Нет')], default=False, verbose_name='Близость с метро'),
        ),
        migrations.AlterField(
            model_name='kvartiravtorichkaarenda',
            name='blizost_so_shkoloi',
            field=models.BooleanField(choices=[(None, '---'), (True, 'Да'), (False, 'Нет')], default=False, verbose_name='Близость со школой'),
        ),
        migrations.AlterField(
            model_name='kvartiravtorichkaarenda',
            name='nalichie_gaza',
            field=models.BooleanField(choices=[(None, '---'), (True, 'Да'), (False, 'Нет')], default=False, verbose_name='Наличие газа в доме'),
        ),
        migrations.AlterField(
            model_name='kvartiravtorichkaprodaza',
            name='akzia',
            field=models.BooleanField(default=False, editable=False, verbose_name='Акция/спец цена'),
        ),
        migrations.AlterField(
            model_name='nezeliearenda',
            name='akzia',
            field=models.BooleanField(default=False, editable=False, verbose_name='Акция/спец цена'),
        ),
        migrations.AlterField(
            model_name='nezeliearenda',
            name='blizost_s_med',
            field=models.BooleanField(choices=[(None, '---'), (True, 'Да'), (False, 'Нет')], default=False, verbose_name='Близость с мед учереждением'),
        ),
        migrations.AlterField(
            model_name='nezeliearenda',
            name='blizost_s_metro',
            field=models.BooleanField(choices=[(None, '---'), (True, 'Да'), (False, 'Нет')], default=False, verbose_name='Близость с метро'),
        ),
        migrations.AlterField(
            model_name='nezeliearenda',
            name='blizost_so_shkoloi',
            field=models.BooleanField(choices=[(None, '---'), (True, 'Да'), (False, 'Нет')], default=False, verbose_name='Близость со школой'),
        ),
        migrations.AlterField(
            model_name='nezeliearenda',
            name='nalichie_gaza',
            field=models.BooleanField(choices=[(None, '---'), (True, 'Да'), (False, 'Нет')], default=False, verbose_name='Наличие газа в доме'),
        ),
        migrations.AlterField(
            model_name='nezelieprodaza',
            name='akzia',
            field=models.BooleanField(default=False, editable=False, verbose_name='Акция/спец цена'),
        ),
        migrations.AlterField(
            model_name='uchactkiarenda',
            name='akzia',
            field=models.BooleanField(default=False, editable=False, verbose_name='Акция/спец цена'),
        ),
        migrations.AlterField(
            model_name='uchactkiarenda',
            name='blizost_s_med',
            field=models.BooleanField(choices=[(None, '---'), (True, 'Да'), (False, 'Нет')], default=False, verbose_name='Близость с мед учереждением'),
        ),
        migrations.AlterField(
            model_name='uchactkiarenda',
            name='blizost_s_metro',
            field=models.BooleanField(choices=[(None, '---'), (True, 'Да'), (False, 'Нет')], default=False, verbose_name='Близость с метро'),
        ),
        migrations.AlterField(
            model_name='uchactkiarenda',
            name='blizost_so_shkoloi',
            field=models.BooleanField(choices=[(None, '---'), (True, 'Да'), (False, 'Нет')], default=False, verbose_name='Близость со школой'),
        ),
        migrations.AlterField(
            model_name='uchactkiarenda',
            name='nalichie_gaza',
            field=models.BooleanField(choices=[(None, '---'), (True, 'Да'), (False, 'Нет')], default=False, verbose_name='Наличие газа в доме'),
        ),
        migrations.AlterField(
            model_name='uchactkiprodaza',
            name='akzia',
            field=models.BooleanField(default=False, editable=False, verbose_name='Акция/спец цена'),
        ),
    ]