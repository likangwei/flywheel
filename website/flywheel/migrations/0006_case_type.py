# Generated by Django 3.1 on 2020-09-02 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flywheel', '0005_case'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='type',
            field=models.CharField(choices=[('good', 'good'), ('bad', 'bad')], default='good', max_length=20),
            preserve_default=False,
        ),
    ]
