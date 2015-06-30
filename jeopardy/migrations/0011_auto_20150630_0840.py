# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jeopardy', '0010_auto_20150630_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonusquestion',
            name='value',
            field=models.IntegerField(verbose_name='Points'),
        ),
    ]
