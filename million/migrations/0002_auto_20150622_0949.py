# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('million', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'verbose_name': 'Game', 'verbose_name_plural': 'Games'},
        ),
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_four',
            field=models.CharField(max_length=50, verbose_name='Fourth Answer'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_four_correct',
            field=models.BooleanField(verbose_name='Fourth Answer is Correct'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_one',
            field=models.CharField(max_length=50, verbose_name='First Answer'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_one_correct',
            field=models.BooleanField(verbose_name='First Answer is Correct'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_three',
            field=models.CharField(max_length=50, verbose_name='Third Answer'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_three_correct',
            field=models.BooleanField(verbose_name='Third Answer is Correct'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_two',
            field=models.CharField(max_length=50, verbose_name='Second Answer'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_two_correct',
            field=models.BooleanField(verbose_name='Second Answer is Correct'),
        ),
        migrations.AlterField(
            model_name='question',
            name='game',
            field=models.ForeignKey(verbose_name='Game', to='million.Game'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=255, verbose_name='Question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='value',
            field=models.IntegerField(verbose_name='Value'),
        ),
    ]
