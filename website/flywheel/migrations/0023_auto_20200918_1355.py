# Generated by Django 3.1 on 2020-09-18 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flywheel', '0022_auto_20200918_1343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='copy',
            name='depends',
        ),
        migrations.AddField(
            model_name='copy',
            name='downstreams',
            field=models.ManyToManyField(blank=True, to='flywheel.Copy'),
        ),
        migrations.AlterField(
            model_name='copy',
            name='depend',
            field=models.TextField(blank=True, help_text='基础依赖'),
        ),
        migrations.AlterField(
            model_name='copy',
            name='rate',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='copy',
            name='rate_one_year',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
