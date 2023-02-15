# Generated by Django 2.2.5 on 2023-02-15 09:20

import basic_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0018_records_cash'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cash', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='records',
            name='cash',
            field=models.BooleanField(default=False, validators=[basic_app.models.cashTick]),
        ),
    ]
