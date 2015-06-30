# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jeopardy', '0005_auto_20150629_0810'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]
