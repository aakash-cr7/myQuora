# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('text', models.CharField(max_length=1024)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_spam', models.BooleanField(default=False)),
                ('by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('downvoted_by', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, related_name='answers_downvoted')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=256)),
                ('desc', models.CharField(max_length=1024, default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=40)),
                ('url', models.URLField(max_length=100, default='')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='topics',
            field=models.ManyToManyField(to='question.Topic'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(related_name='answers', to='question.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='upvoted_by',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, related_name='answers_upvoted'),
        ),
    ]
