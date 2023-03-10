# Generated by Django 2.2.5 on 2023-02-15 05:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0016_auto_20230214_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountheads',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='accountheads',
            name='status',
            field=models.CharField(blank=True, default='Active', max_length=100),
        ),
        migrations.AlterField(
            model_name='records',
            name='date',
            field=models.DateField(default=datetime.date(2023, 2, 15)),
        ),
    ]
