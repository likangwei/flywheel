# Generated by Django 3.0.7 on 2020-06-25 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('replay', '0004_auto_20200625_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='replay',
            name='create_time',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='replay',
            name='tags',
            field=models.ManyToManyField(blank=True, to='replay.Tag'),
        ),
    ]
