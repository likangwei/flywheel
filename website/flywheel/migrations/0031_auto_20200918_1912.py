# Generated by Django 3.1 on 2020-09-18 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flywheel', '0030_auto_20200918_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='situation',
            field=models.TextField(default='', help_text='背景'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='goal',
            name='goal',
            field=models.TextField(help_text='目标、量化'),
        ),
    ]
