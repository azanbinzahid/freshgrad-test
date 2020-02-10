# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2020-02-03 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freshgrad_test', '0011_auto_20200131_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateinfo',
            name='biggest_accomplishment',
            field=models.TextField(verbose_name='Your biggest acomplishment to-date?'),
        ),
        migrations.AlterField(
            model_name='candidateinfo',
            name='extra_activities',
            field=models.TextField(verbose_name="List down any extra curricular activitiez you're involved in(if any)?"),
        ),
        migrations.AlterField(
            model_name='candidateinfo',
            name='makes_me_different',
            field=models.TextField(max_length=8, verbose_name='What makes you different from your batch mates?'),
        ),
    ]