# Generated by Django 3.2.3 on 2024-02-15 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0003_alter_currencyrate_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currencyrate',
            options={'ordering': ('-date', 'charcode'), 'verbose_name': 'Курс валюты', 'verbose_name_plural': 'Курсы валют'},
        ),
    ]
