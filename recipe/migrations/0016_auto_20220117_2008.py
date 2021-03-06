# Generated by Django 3.2.2 on 2022-01-17 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0015_auto_20211030_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sub_recipe',
            name='archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='outlet',
            field=models.CharField(choices=[('The Nest', 'Afternoon Tea'), ('Madara', 'Madara'), ('Pizza Mozzo', 'Banqueting'), ('breakfast', 'Breakfast'), ('Room Service', 'Room Service'), ('Recipes', 'Recipes'), ('Amenities', 'Amenities')], max_length=100),
        ),
    ]
