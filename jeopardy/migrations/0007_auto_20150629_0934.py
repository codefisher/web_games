# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jeopardy.models


class Migration(migrations.Migration):

    dependencies = [
        ('jeopardy', '0006_game_hidden'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bonusquestion',
            options={'verbose_name': 'Final Question', 'verbose_name_plural': 'Final Question'},
        ),
        migrations.AddField(
            model_name='bonusquestion',
            name='correct_picture',
            field=models.ImageField(upload_to=jeopardy.models.question_image_path, null=True, verbose_name='Picture When Correct', blank=True),
        ),
        migrations.AddField(
            model_name='bonusquestion',
            name='wrong_picture',
            field=models.ImageField(upload_to=jeopardy.models.question_image_path, null=True, verbose_name='Picture When Wrong', blank=True),
        ),
    ]
