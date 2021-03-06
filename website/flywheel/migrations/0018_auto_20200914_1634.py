# Generated by Django 3.1 on 2020-09-14 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flywheel', '0017_auto_20200910_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='copy',
            name='status',
            field=models.CharField(choices=[('on', 'on'), ('dev', 'dev'), ('off', 'off')], default='off', max_length=200),
        ),
    ]
