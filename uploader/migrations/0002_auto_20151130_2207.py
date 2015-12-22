# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sourcefile',
            name='filename',
        ),
        migrations.RemoveField(
            model_name='sourcefile',
            name='nickname',
        ),
        migrations.AddField(
            model_name='sourcefile',
            name='datafile',
            field=models.FileField(default='default text', upload_to=b'datafiles/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
