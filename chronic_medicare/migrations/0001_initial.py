# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisFile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=512)),
                ('csv_file', models.FileField(upload_to='analysis-files/')),
                ('description', models.TextField(blank=True, max_length=1024)),
            ],
            options={
                'verbose_name_plural': 'Raw Analysis Files',
            },
        ),
    ]
