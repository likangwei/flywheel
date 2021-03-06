# Generated by Django 3.0.7 on 2020-06-27 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('replay', '0009_remove_roadblock_cycle'),
    ]

    operations = [
        migrations.CreateModel(
            name='RootCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(blank=True)),
                ('road_block', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='replay.RoadBlock')),
            ],
        ),
        migrations.DeleteModel(
            name='DiagnoseRootCase',
        ),
    ]
