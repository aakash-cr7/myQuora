# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'User'},
        ),
        migrations.AddField(
            model_name='customuser',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='following',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True, related_name='followers'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('NS', 'Not Set')], max_length=2, default='NS'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(unique=True, max_length=11, default=''),
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pics/'),
        ),
        migrations.AlterUniqueTogether(
            name='customuser',
            unique_together=set([('email',)]),
        ),
    ]
