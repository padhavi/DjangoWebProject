# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_auto_20170415_1728'),
    ]

    operations = [
        migrations.CreateModel(
            name='fcomplain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('complain', models.CharField(max_length=250)),
                ('status_update', models.CharField(max_length=250)),
                ('f', models.ForeignKey(to='homepage.farmer')),
            ],
        ),
    ]
