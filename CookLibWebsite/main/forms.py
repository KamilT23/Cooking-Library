from django.forms import ModelForm, TextInput, PasswordInput, Textarea, Select, SelectMultiple, NumberInput, \
    MultipleChoiceField, ModelMultipleChoiceField, CheckboxSelectMultiple
from .models import *

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='@', widget=forms.TextInput(attrs={
                'aria - label' : 'Login',
                'class': 'form-control',
                'placeholder': 'Введите ваш логин'
            }))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                  'placeholder': 'Введите пароль', }))

class UserForm(UserCreationForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'Введите пароль', }))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                        'placeholder': 'Введите пароль',}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

        widgets = {
            "first_name": TextInput(attrs={
                'aria - label' : 'First name',
                'class': 'form-control',
                'placeholder': 'Введите ваше имя'
            }),
            "last_name": TextInput(attrs={
                'aria - label' : 'Last name',
                'class': 'form-control',
                'placeholder': 'Введите вашу фамилию'
            }),
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваш логин',
                'aria - label': 'Username',
                'aria - describedby': 'addon-wrapping'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'name@example.com',
                'aria - label' : 'Username',
                'aria - describedby' : 'addon-wrapping'
            }),
        }

class AddFavRecForm(ModelForm):
    class Meta:
        model = recipe
        fields = ['fav_recs']
        widgets = {
            "fav_recs": SelectMultiple(attrs={
            'class': 'select2bs4 select2-hidden-accessible form-control',
            'multiple': '',
            'tabindex': '-1',
            'aria-hidden': 'true'
        })
        }

class AddRecipeForm(ModelForm):

    class Meta:
        model = recipe
        fields = ['fav_recs','title_recipe', 'count_servings', 'count_calories','need_time','recipe_description', 'need_products', 'category']
        widgets = {
            "category": Select(),
            "title_recipe": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название блюда',
                'aria - describedby': 'addon-wrapping'
            }),
            "count_calories": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите калорийность блюда',
                'aria - describedby': 'addon-wrapping'
            }),
            "count_servings": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите количество порций',
                'aria - describedby': 'addon-wrapping'
            }),
            "need_time": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите количество минут',
                'aria - describedby': 'addon-wrapping'
            }),
            "need_products": SelectMultiple(attrs={
        'class': 'select2bs4 select2-hidden-accessible form-control',
        'multiple': '',
        'tabindex': '-1',
        'aria-hidden': 'true'
    }),
            "fav_recs": SelectMultiple(attrs={
                'class': 'select2bs4 select2-hidden-accessible form-control',
                'multiple': '',
                'tabindex': '-1',
                'aria-hidden': 'true'
            }),
            "recipe_description": Textarea(attrs={
                'id' : 'recipe',
                'rows': '7',
                'cols': '54'
            }),
        }

class AddProductForm(ModelForm):
    class Meta:
        model = products
        fields = ['name_product', 'product_calories','mass']
        widgets = {
            "name_product": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название продукта',
                'aria - describedby': 'addon-wrapping'
            }),
            "product_calories": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество ккал в ингредиенте',
                'aria - describedby': 'addon-wrapping'
            }),
            "mass": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество (г)',
                'aria - describedby': 'addon-wrapping'
            })
        }
