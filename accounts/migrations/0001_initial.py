# Generated by Django 2.1.5 on 2019-01-26 17:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='Email Address')),
                ('full_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Full Name')),
                ('fingercode', models.CharField(blank=True, max_length=10, null=True)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2019, 1, 26, 17, 11, 54, 534206, tzinfo=utc), verbose_name='Registered Date')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]