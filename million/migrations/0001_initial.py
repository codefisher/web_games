# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=255)),
                ('value', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('answer_one', models.CharField(max_length=50)),
                ('answer_one_correct', models.BooleanField()),
                ('answer_two', models.CharField(max_length=50)),
                ('answer_two_correct', models.BooleanField()),
                ('answer_three', models.CharField(max_length=50)),
                ('answer_three_correct', models.BooleanField()),
                ('answer_four', models.CharField(max_length=50)),
                ('answer_four_correct', models.BooleanField()),
                ('game', models.ForeignKey(to='million.Game')),
            ],
        ),
    ]
