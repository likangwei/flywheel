# Generated by Django 3.1 on 2020-09-02 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flywheel', '0004_auto_20200828_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(blank=True)),
            ],
        ),
    ]
