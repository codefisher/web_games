# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BonusQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=255, verbose_name='Question')),
                ('answer', models.CharField(max_length=255, verbose_name='Answer')),
                ('value', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Bonus Question',
                'verbose_name_plural': 'Bonus Question',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Game',
                'verbose_name_plural': 'Games',
            },
        ),
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.IntegerField()),
                ('game', models.ForeignKey(related_name='points', verbose_name='Game', to='jeopardy.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=255, verbose_name='Question')),
                ('answer', models.CharField(max_length=255, verbose_name='Answer')),
                ('game', models.ForeignKey(related_name='questions', verbose_name='Game', to='jeopardy.Game')),
                ('points', models.ForeignKey(related_name='points', verbose_name='Points', to='jeopardy.Points')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('game', models.ForeignKey(related_name='topic', verbose_name='Game', to='jeopardy.Game')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.ForeignKey(related_name='topic', verbose_name='Topic', to='jeopardy.Topic'),
        ),
        migrations.AddField(
            model_name='bonusquestion',
            name='game',
            field=models.ForeignKey(related_name='bonus_question', verbose_name='Game', to='jeopardy.Game'),
        ),
    ]
