# Generated by Django 4.2.7 on 2023-11-05 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('value', models.FloatField()),
            ],
        ),
    ]
