# Generated by Django 4.1.7 on 2023-06-01 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_profile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='favorite_recipes',
            field=models.ManyToManyField(blank=True, null=True, to='main.recipe', verbose_name='Избранные рецепты'),
        ),
    ]
