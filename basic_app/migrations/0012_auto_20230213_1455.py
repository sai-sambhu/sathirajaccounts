# Generated by Django 2.2.5 on 2023-02-13 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0011_auto_20230213_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='records',
            name='appuid',
        ),
        migrations.RemoveField(
            model_name='records',
            name='status',
        ),
    ]
