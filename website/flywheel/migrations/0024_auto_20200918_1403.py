# Generated by Django 3.1 on 2020-09-18 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flywheel', '0023_auto_20200918_1355'),
    ]

    operations = [
        migrations.RenameField(
            model_name='copy',
            old_name='downstreams',
            new_name='depends',
        ),
    ]
