# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jeopardy', '0016_bonusquestion_picture_reveal'),
    ]

    operations = [
        migrations.AddField(
            model_name='bonusquestion',
            name='reveal_time',
            field=models.IntegerField(default=10, verbose_name='Picture Reveal Seconds'),
        ),
        migrations.AddField(
            model_name='question',
            name='reveal_time',
            field=models.IntegerField(default=10, verbose_name='Picture Reveal Seconds'),
        ),
    ]
