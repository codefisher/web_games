# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jeopardy', '0002_auto_20150622_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(max_length=255, null=True, verbose_name='Answer', blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='points',
            field=models.ForeignKey(related_name='points', verbose_name='Points', to='jeopardy.Points', null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=255, null=True, verbose_name='Question', blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='topic',
            field=models.ForeignKey(related_name='topicopi', verbose_name='Topic', to='jeopardy.Topic', null=True),
        ),
    ]
