# Generated by Django 3.1 on 2020-09-18 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flywheel', '0029_auto_20200918_1859'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goal',
            old_name='title',
            new_name='goal',
        ),
    ]