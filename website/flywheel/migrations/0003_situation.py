# Generated by Django 3.0.7 on 2020-06-28 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flywheel', '0002_wheelpart_next_part'),
    ]

    operations = [
        migrations.CreateModel(
            name='Situation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('situation', models.CharField(max_length=300)),
                ('principle', models.TextField(blank=True)),
                ('sop', models.TextField(blank=True)),
            ],
        ),
    ]
