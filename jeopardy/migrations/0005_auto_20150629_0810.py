# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jeopardy.models


class Migration(migrations.Migration):

    dependencies = [
        ('jeopardy', '0004_auto_20150623_0805'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='win_picture',
            field=models.ImageField(upload_to=jeopardy.models.question_image_path, null=True, verbose_name='Picture At Victory', blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='correct_picture',
            field=models.ImageField(upload_to=jeopardy.models.question_image_path, null=True, verbose_name='Picture When Correct', blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='wrong_picture',
            field=models.ImageField(upload_to=jeopardy.models.question_image_path, null=True, verbose_name='Picture When Wrong', blank=True),
        ),
    ]
