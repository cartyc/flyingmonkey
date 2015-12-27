# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('street', models.CharField(blank=True, max_length=255, null=True)),
                ('streetType', models.CharField(blank=True, max_length=20, null=True)),
                ('municipality', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='mainParcel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pin', models.CharField(max_length=9)),
                ('roll', models.CharField(blank=True, max_length=10, null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True)),
                ('mainAddress', models.ForeignKey(to='property.address', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='subordParcel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pin', models.ForeignKey(to='property.mainParcel')),
            ],
        ),
    ]
