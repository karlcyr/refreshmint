# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_auto_20151104_2250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match_Rules',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('matchtext', models.CharField(max_length=200, verbose_name=b'text to match')),
                ('friendly', models.CharField(max_length=100, verbose_name=b'friendly description')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.ForeignKey(to='transactions.Category', null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='friendly',
            field=models.CharField(max_length=100, verbose_name=b'friendly description', blank=True),
        ),
    ]
