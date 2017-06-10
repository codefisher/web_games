# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jeopardy', '0015_auto_20170610_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='bonusquestion',
            name='picture_reveal',
            field=models.BooleanField(default=False, verbose_name='Slowly Reveal Picture'),
        ),
    ]
