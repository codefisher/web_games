# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jeopardy', '0011_auto_20150630_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonusquestion',
            name='value',
            field=models.IntegerField(default=0, verbose_name='Points'),
            preserve_default=False,
        ),
    ]
