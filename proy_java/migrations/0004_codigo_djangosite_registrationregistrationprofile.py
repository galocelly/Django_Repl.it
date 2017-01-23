# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 01:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proy_java', '0003_delete_codigo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Codigo',
            fields=[
                ('id_codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('link', models.CharField(blank=True, max_length=250, null=True)),
                ('cod_fuente', models.CharField(blank=True, max_length=2000, null=True)),
            ],
            options={
                'db_table': 'codigo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'django_site',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RegistrationRegistrationprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activation_key', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'registration_registrationprofile',
                'managed': False,
            },
        ),
    ]
