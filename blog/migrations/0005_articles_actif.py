# Generated by Django 3.2.18 on 2023-06-13 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_articles_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='actif',
            field=models.BooleanField(default=True),
        ),
    ]
