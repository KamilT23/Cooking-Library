# Generated by Django 4.1.7 on 2023-05-28 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_products_mass'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Категория'),
        ),
    ]
