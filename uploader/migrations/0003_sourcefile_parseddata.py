# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0002_auto_20151130_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='sourcefile',
            name='parseddata',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
