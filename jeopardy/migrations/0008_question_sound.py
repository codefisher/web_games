# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jeopardy.models


class Migration(migrations.Migration):

    dependencies = [
        ('jeopardy', '0007_auto_20150629_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='sound',
            field=models.FileField(upload_to=jeopardy.models.question_image_path, null=True, verbose_name='Sound', blank=True),
        ),
    ]
