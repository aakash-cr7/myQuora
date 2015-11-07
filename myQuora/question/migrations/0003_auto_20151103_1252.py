# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_auto_20151103_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='questions_asked'),
        ),
    ]
