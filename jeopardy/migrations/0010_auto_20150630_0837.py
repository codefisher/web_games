# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jeopardy', '0009_auto_20150630_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='bonus',
            field=models.IntegerField(default=0, verbose_name='Bonus Points'),
        ),
    ]
