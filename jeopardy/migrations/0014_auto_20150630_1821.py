# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jeopardy', '0013_auto_20150630_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='countdown_seconds',
            field=models.IntegerField(default=20, verbose_name='Number of seconds to Count down'),
        ),
        migrations.AddField(
            model_name='game',
            name='use_countdown',
            field=models.BooleanField(default=True, verbose_name='Use Count down Timer'),
        ),
        migrations.AlterField(
            model_name='game',
            name='hidden',
            field=models.BooleanField(default=False, verbose_name='Hidden'),
        ),
    ]
