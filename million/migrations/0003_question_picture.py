# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import million.models


class Migration(migrations.Migration):

    dependencies = [
        ('million', '0002_auto_20150622_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='picture',
            field=models.ImageField(upload_to=million.models.question_image_path, null=True, verbose_name='Picture', blank=True),
        ),
    ]
