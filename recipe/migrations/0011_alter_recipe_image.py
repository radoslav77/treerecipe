# Generated by Django 3.2.2 on 2021-05-17 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0010_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.URLField(default=None, null=True),
        ),
    ]