# Generated by Django 5.1.1 on 2024-10-14 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0006_alter_product_options_alter_product_is_published"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="is_published",
            field=models.BooleanField(default=False, verbose_name="Опубликован"),
        ),
    ]