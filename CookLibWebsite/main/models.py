from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from slugify import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver

"""Таблица пользователей"""
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    favorite_recipes = models.ManyToManyField('recipe', verbose_name='Избранные рецепты', blank=True, null=True)
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def get_absolute_url(self):
        return f'/profile'

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'


"""Таблица рецептов"""
class recipe(models.Model):
    title_recipe = models.CharField('Название рецепта', max_length=150)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", blank=True, null=True)
    count_servings = models.IntegerField('Количество порций', null=True, blank=True)
    count_calories = models.FloatField('Количество ККал', null=True, blank=True)
    need_time = models.IntegerField('Время готовки (в минутах)', null=True, blank=True)
    recipe_description = models.TextField('Описание рецепта')
    need_products = models.ManyToManyField('products', verbose_name='Необходимые продукты')
    CAT_CHOICES = [
        ('1', 'Завтраки'), ('2', 'Основные блюда'), ('3', 'Закуски'),
        ('4', 'Супы'), ('5', 'Салаты'), ('6', 'Выпечка и десерты')
    ]
    category = models.CharField(max_length=150, choices=CAT_CHOICES, default='1')
    fav_recs = models.ManyToManyField(User, verbose_name="Избранные рецепты", blank=True)

    def __str__(self):
        return self.title_recipe
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title_recipe)
        return super(recipe, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/recipe/{self.slug}'

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    # def create_recipe(self):
    #     test_product11 = products.objects.all()
    #     test_recipe = self
    #     test_recipe.save()
    #     test_recipe.need_products.add(test_product11[0], test_product11[4], test_product11[10])
    #     test_recipe.save()

"""Таблица продуктов"""
class products(models.Model):
    name_product = models.CharField('Название продукта', max_length=100, db_index=True)
    mass = models.FloatField('Количество в гр', null=True)
    product_calories = models.FloatField('Количество ккал в продукте')

    def __str__(self):
        return self.name_product

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'