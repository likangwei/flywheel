# Generated by Django 3.0.7 on 2020-06-28 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('replay', '0011_auto_20200628_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cycle',
            name='blocks',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='cycle',
            name='root_case',
            field=models.TextField(blank=True),
        ),
    ]
