# Generated by Django 5.1.3 on 2024-11-12 06:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fluke',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.IntegerField(unique=True, verbose_name='S/N')),
                ('IP', models.CharField(max_length=15, verbose_name='IP')),
            ],
            options={
                'verbose_name': 'Эталон',
                'verbose_name_plural': 'Эталоны',
            },
        ),
        migrations.CreateModel(
            name='Charm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.IntegerField(unique=True, verbose_name='S/N')),
                ('calibrator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='charm.fluke', verbose_name='Калибратор')),
            ],
            options={
                'verbose_name': 'Чарм',
                'verbose_name_plural': 'Чармы',
            },
        ),
    ]