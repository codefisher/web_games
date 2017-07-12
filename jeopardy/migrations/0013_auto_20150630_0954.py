# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('jeopardy', '0012_bonusquestion_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Player Name')),
                ('points', models.IntegerField(verbose_name='Points')),
            ],
            options={
                'verbose_name': 'Player',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Time', blank=True)),
                ('game', models.ForeignKey(related_name='results', verbose_name='Result', to='jeopardy.Game', on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'Result',
            },
        ),
        migrations.AlterField(
            model_name='points',
            name='value',
            field=models.IntegerField(verbose_name='Value'),
        ),
        migrations.AddField(
            model_name='player',
            name='result',
            field=models.ForeignKey(verbose_name='Result', to='jeopardy.Result', on_delete=models.CASCADE),
        ),
    ]
