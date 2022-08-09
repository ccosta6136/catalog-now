# Generated by Django 4.0.5 on 2022-08-08 22:44

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('social_network_twitter', models.URLField(null=True)),
                ('social_network_instagram', models.URLField(null=True)),
                ('social_network_linkedin', models.URLField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('address', models.CharField(max_length=80, null=True)),
                ('city', models.CharField(max_length=80, null=True)),
                ('zip_code', models.CharField(max_length=20, null=True)),
                ('country', models.CharField(max_length=80, null=True)),
                ('phone', models.CharField(max_length=30, null=True)),
                ('whatsapp_phone_number', models.CharField(max_length=30, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='avatars')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=100)),
                ('short_description', models.CharField(max_length=180)),
                ('description', ckeditor.fields.RichTextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='catalog_now_app.publisher')),
            ],
        ),
    ]
