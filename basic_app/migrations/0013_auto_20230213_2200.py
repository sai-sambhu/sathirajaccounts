# Generated by Django 2.2.5 on 2023-02-13 16:30

import basic_app.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0012_auto_20230213_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountheads',
            name='name',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='records',
            name='credit',
            field=models.IntegerField(blank=True, default=0, validators=[basic_app.models.credit]),
        ),
        migrations.AlterField(
            model_name='records',
            name='date',
            field=models.DateField(default=datetime.date(2023, 2, 13)),
        ),
        migrations.AlterField(
            model_name='records',
            name='debit',
            field=models.IntegerField(blank=True, default=0, validators=[basic_app.models.creditDebitValidator]),
        ),
    ]
