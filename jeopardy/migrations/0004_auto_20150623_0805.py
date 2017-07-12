# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jeopardy.models


class Migration(migrations.Migration):

    dependencies = [
        ('jeopardy', '0003_auto_20150622_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='bonusquestion',
            name='picture',
            field=models.ImageField(upload_to=jeopardy.models.question_image_path, null=True, verbose_name='Picture', blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='picture',
            field=models.ImageField(upload_to=jeopardy.models.question_image_path, null=True, verbose_name='Picture', blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='topic',
            field=models.ForeignKey(related_name='topic', verbose_name='Topic', to='jeopardy.Topic', null=True, on_delete=models.CASCADE),
        ),
    ]
