# Generated by Django 4.0.4 on 2022-08-05 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_now_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='address',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='catalog',
            name='city',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='catalog',
            name='country',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='catalog',
            name='phone',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='catalog',
            name='social_network_three',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='catalog',
            name='zip_code',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
