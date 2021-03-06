# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 14:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20170825_1114'),
        ('annotations', '0009_auto_20170826_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExportFormat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('public', models.BooleanField(default=False)),
                ('base_format', models.TextField()),
                ('annotation_format', models.TextField()),
                ('annotations_types', models.ManyToManyField(to='annotations.AnnotationType')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='export_formats', to='users.Team')),
            ],
        ),
        migrations.AddField(
            model_name='export',
            name='format',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='exports', to='annotations.ExportFormat'),
            preserve_default=False,
        ),
    ]
