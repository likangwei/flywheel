# Generated by Django 3.1 on 2020-09-18 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flywheel', '0028_auto_20200918_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='title',
            field=models.TextField(help_text='背景、目标、量化'),
        ),
    ]