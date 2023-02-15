# Generated by Django 2.2.5 on 2023-02-13 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0006_auto_20230213_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountHeads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('phone', models.IntegerField(blank=True, max_length=10)),
                ('address', models.CharField(blank=True, max_length=5)),
                ('status', models.CharField(blank=True, default='Active', max_length=15)),
            ],
        ),
    ]