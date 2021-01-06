# Generated by Django 3.1 on 2020-09-22 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flywheel', '0033_auto_20200921_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='copy',
            name='check_rate',
            field=models.CharField(default='0 0 * * *', max_length=200),
        ),
        migrations.AlterField(
            model_name='goal',
            name='solution',
            field=models.TextField(blank=True, help_text='方案，倒推或一招制胜'),
        ),
    ]