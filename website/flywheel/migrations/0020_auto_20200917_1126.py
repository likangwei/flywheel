# Generated by Django 3.1 on 2020-09-17 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flywheel', '0019_auto_20200917_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='copy',
            name='how',
            field=models.TextField(default='', help_text='如何做'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='copy',
            name='depend',
            field=models.TextField(help_text='基础依赖'),
        ),
    ]