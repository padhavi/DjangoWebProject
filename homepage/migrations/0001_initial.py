# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='crop',
            fields=[
                ('cropid', models.AutoField(serialize=False, primary_key=True)),
                ('cname', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='f_ad_details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('crop_details', models.ForeignKey(to='homepage.crop')),
            ],
        ),
        migrations.CreateModel(
            name='farmer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=500)),
                ('crop_details', models.ForeignKey(to='homepage.crop')),
            ],
        ),
        migrations.CreateModel(
            name='fcomplain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('f', models.ForeignKey(to='homepage.farmer')),
            ],
        ),
        migrations.CreateModel(
            name='qty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fid', models.CharField(max_length=250)),
                ('crop_details', models.ForeignKey(to='homepage.crop')),
            ],
        ),
        migrations.CreateModel(
            name='r_ad_details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('crop_details', models.ForeignKey(to='homepage.crop')),
                ('qty_details', models.ForeignKey(to='homepage.qty')),
            ],
        ),
        migrations.CreateModel(
            name='rcomplain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='retailer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rname', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='sell',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('crop_details', models.ForeignKey(to='homepage.crop')),
                ('farmer_details', models.ForeignKey(to='homepage.farmer')),
                ('qty_sold_at', models.ForeignKey(to='homepage.qty')),
                ('retailer_details', models.ForeignKey(to='homepage.retailer')),
            ],
        ),
        migrations.AddField(
            model_name='rcomplain',
            name='r',
            field=models.ForeignKey(to='homepage.retailer'),
        ),
        migrations.AddField(
            model_name='r_ad_details',
            name='retailer_details',
            field=models.ForeignKey(to='homepage.retailer'),
        ),
        migrations.AddField(
            model_name='f_ad_details',
            name='farmer_details',
            field=models.ForeignKey(to='homepage.farmer'),
        ),
        migrations.AddField(
            model_name='f_ad_details',
            name='qty_details',
            field=models.ForeignKey(to='homepage.qty'),
        ),
    ]
