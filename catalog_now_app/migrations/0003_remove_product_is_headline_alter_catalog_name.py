# Generated by Django 4.0.5 on 2022-08-08 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_now_app', '0002_catalog_address_catalog_city_catalog_country_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_headline',
        ),
        migrations.AlterField(
            model_name='catalog',
            name='name',
            field=models.CharField(max_length=90),
        ),
    ]
