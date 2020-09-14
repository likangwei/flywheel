# Generated by Django 3.1 on 2020-09-04 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flywheel', '0010_situation_sys_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='flywheel',
            name='best',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flywheel',
            name='worse',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='situation',
            name='sys_level',
            field=models.IntegerField(choices=[(3, '高'), (2, '中'), (1, '低'), (0, '无')], default=0),
        ),
    ]
