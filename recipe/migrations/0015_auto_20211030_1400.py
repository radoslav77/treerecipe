# Generated by Django 3.2.2 on 2021-10-30 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0014_auto_20211030_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='archived',
        ),
        migrations.RemoveField(
            model_name='sub_recipe',
            name='archived',
        ),
    ]
