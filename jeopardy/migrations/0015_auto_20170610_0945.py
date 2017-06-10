# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jeopardy', '0014_auto_20150630_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='picture_reveal',
            field=models.BooleanField(default=False, verbose_name='Slowly Reveal Picture'),
        ),
        migrations.AlterField(
            model_name='game',
            name='countdown_seconds',
            field=models.IntegerField(default=10, verbose_name='Number of seconds to Count down'),
        ),
    ]
