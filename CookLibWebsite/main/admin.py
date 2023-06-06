from django.contrib import admin
from .models import *

class recipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_recipe', 'count_servings', 'count_calories', 'need_time','category') #эти поля будут отображаться в админ панеле
    list_display_links = ('id', 'title_recipe') #по этим полям можно будет кликать для дальнейшего изменения
    search_fields = ('title_recipe', 'count_servings') #по каким полям можно будет производить поиск информации
    prepopulated_fields = {"slug": ("title_recipe",)}

class productsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_product', 'product_calories') #эти поля будут отображаться в админ панеле
    list_display_links = ('id', 'name_product') #по этим полям можно будет кликать для дальнейшего изменения

class profileAdmin(admin.ModelAdmin):
    list_display = ('id',) #эти поля будут отображаться в админ панеле
    list_display_links = ('id',) #по этим полям можно будет кликать для дальнейшего изменения
    search_fields = ('title_recipe', 'count_servings') #по каким полям можно будет производить поиск информации
    #prepopulated_fields = {"slug": ("user.last_name","user.first_name",)}


admin.site.register(recipe, recipeAdmin)
admin.site.register(products, productsAdmin)
admin.site.register(profile, profileAdmin)