# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(verbose_name=b'transaction date')),
                ('raw', models.CharField(max_length=200, verbose_name=b'raw description')),
                ('friendly', models.CharField(max_length=100, verbose_name=b'friendly description')),
                ('amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('category', models.ForeignKey(to='transactions.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
