# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-29 12:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=200)),
                ('contact_info', models.CharField(blank=True, max_length=200)),
                ('profile_Id', models.IntegerField(default=0)),
                ('profile_picture', models.ImageField(default='user.png', upload_to='users/')),
                ('bio', models.TextField(default='Welcome!')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
