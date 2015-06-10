# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='gameCats',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='publisher',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='ratedInfo',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='title',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
