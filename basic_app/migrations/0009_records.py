# Generated by Django 2.2.5 on 2023-02-13 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0008_auto_20230213_1250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True)),
                ('credit', models.IntegerField(blank=True)),
                ('debit', models.IntegerField(blank=True)),
                ('remarks', models.CharField(blank=True, max_length=15)),
                ('status', models.CharField(blank=True, default='Active', max_length=15)),
                ('appuid', models.CharField(blank=True, max_length=15)),
                ('accountHeads', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic_app.AccountHeads')),
            ],
        ),
    ]
