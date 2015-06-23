# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jeopardy', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='points',
            options={'verbose_name': 'Points', 'verbose_name_plural': 'Points'},
        ),
        migrations.AddField(
            model_name='question',
            name='bonus',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='topic',
            field=models.ForeignKey(related_name='topicopi', verbose_name='Topic', to='jeopardy.Topic'),
        ),
    ]
