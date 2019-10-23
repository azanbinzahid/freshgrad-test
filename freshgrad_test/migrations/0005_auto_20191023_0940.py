# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-23 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freshgrad_test', '0004_auto_20191015_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateinfo',
            name='university',
            field=models.CharField(choices=[(b'COMSATS', 'COMSATS'), (b'University of Engineering & Technology', 'University of Engineering & Technology'), (b'National University of Sciences & Technology', 'National University of Sciences & Technology'), (b'Bahria University', 'Bahria University'), (b'NAMAL', 'NAMAL'), (b'University of Gujrat', 'University of Gujrat'), (b'Islamia University of Bahawalpur', 'Islamia University of Bahawalpur'), (b'PUCIT', 'PUCIT'), (b'GIKI', 'GIKI'), (b'FAST', 'FAST'), (b'Superior University', 'Superior University'), (b'Imperial College', 'Imperial College'), (b'University of Central Punjab', 'University of Central Punjab'), (b'Forman Christian College', 'Forman Christian College'), (b'Szabist', 'Szabist'), (b'Lahore College for Women', 'Lahore College for Women'), (b'University of Lahore', 'University of Lahore'), (b'Kinnaird College', 'Kinnaird College'), (b'University of Management & Technology', 'University of Management & Technology'), (b'AJK University', 'AJK University'), (b'BZU Multan', 'BZU Multan'), (b'Islamia College University', 'Islamia College University'), (b'AIR University', 'AIR University'), (b'Information Technology University', 'Information Technology University'), (b'University of Peshawar', 'University of Peshawar'), (b'Virtual University', 'Virtual University'), (b'Lahore University of Management & Sciences', 'Lahore University of Management & Sciences'), (b'University of Sargodha', 'University of Sargodha'), (b'International Islamic University', 'International Islamic University'), (b'Other', 'Other')], max_length=100),
        ),
    ]
