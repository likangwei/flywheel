# Generated by Django 3.0.7 on 2020-06-25 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('replay', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('replays', models.ManyToManyField(to='replay.Replay')),
            ],
        ),
    ]
