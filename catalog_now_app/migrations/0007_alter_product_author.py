# Generated by Django 4.0.4 on 2022-08-08 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_now_app', '0006_alter_product_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='catalog_now_app.publisher'),
        ),
    ]
