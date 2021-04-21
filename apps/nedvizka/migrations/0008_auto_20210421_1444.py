# Generated by Django 3.0.13 on 2021-04-21 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nedvizka', '0007_auto_20210420_1003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dom',
            name='iframe_panorami',
        ),
        migrations.RemoveField(
            model_name='dom',
            name='video',
        ),
        migrations.CreateModel(
            name='VideoDomov',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.CharField(help_text='Будет выводиться только если выбран шаблонное оформление страницы объекта', max_length=1000, verbose_name='Ссылка на видео youtube')),
                ('index_sortirivki', models.IntegerField(default=0, help_text='Чем больше тем раньше выведет', verbose_name='Индекс сортировки')),
                ('dom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video_set', to='nedvizka.Dom', verbose_name='Дом')),
            ],
            options={
                'verbose_name': 'Видео дома',
                'verbose_name_plural': 'Видео дома',
                'ordering': ['-index_sortirivki'],
            },
        ),
        migrations.CreateModel(
            name='PanoramiDomov',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iframe_code', models.TextField(help_text='Будет выводиться только если выбран шаблонное оформление страницы объекта', verbose_name='iframe код')),
                ('index_sortirivki', models.IntegerField(default=0, help_text='Чем больше тем раньше выведет', verbose_name='Индекс сортировки')),
                ('dom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='panorami_set', to='nedvizka.Dom', verbose_name='Дом')),
            ],
            options={
                'verbose_name': 'Панорамы домов',
                'verbose_name_plural': 'Панорамы домов',
                'ordering': ['-index_sortirivki'],
            },
        ),
    ]