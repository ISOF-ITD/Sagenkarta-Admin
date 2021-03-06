# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-12-09 13:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sagenkarta-Admin', '0017_auto_20191113_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrowdSourceMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[('image', 'Bildfil'), ('pdf', 'Pdf'), ('audio', 'Ljudfil')], max_length=30, null=True)),
                ('source', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'records_media',
                'managed': False,
            },
        ),
        migrations.AlterField(
            model_name='crowdsourceusers',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='importbatch',
            name='batch_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='records',
            name='approvedby',
            field=models.ForeignKey(blank=True, db_column='approvedby', editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Godkänd av'),
        ),
        migrations.AlterField(
            model_name='records',
            name='createdby',
            field=models.ForeignKey(blank=True, db_column='createdby', editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='records_created', to=settings.AUTH_USER_MODEL, verbose_name='Excerperad av'),
        ),
    ]
