# Generated by Django 3.0.13 on 2021-03-28 11:16

from django.db import migrations, models
import django.db.models.deletion
import filer.fields.file


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('filer', '0012_file_mime_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoPlayerJSPluginSetting',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='video_player_js_videoplayerjspluginsetting', serialize=False, to='cms.CMSPlugin')),
                ('video', filer.fields.file.FilerFileField(on_delete=django.db.models.deletion.CASCADE, to='filer.File', verbose_name='Видео')),
            ],
            options={
                'verbose_name': 'Видео плеер JS',
                'verbose_name_plural': 'Видео плеер JS',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
