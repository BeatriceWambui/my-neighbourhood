# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-30 09:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbour', '0007_auto_20191030_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=250)),
                ('address', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='businesses',
            name='neighbourhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='neighbour.Neighbourhood', unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='neighborhood',
            field=models.ForeignKey(blank=True, default='1', on_delete=django.db.models.deletion.CASCADE, to='neighbour.Neighbourhood'),
        ),
    ]
