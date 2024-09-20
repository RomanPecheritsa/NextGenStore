# Generated by Django 5.1.1 on 2024-09-17 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_article_content"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="article",
            options={
                "ordering": ("-created_at",),
                "verbose_name": "статья",
                "verbose_name_plural": "статьи",
            },
        ),
        migrations.AlterField(
            model_name="article",
            name="slug",
            field=models.SlugField(
                blank=True, max_length=200, null=True, unique=True, verbose_name="slug"
            ),
        ),
    ]
