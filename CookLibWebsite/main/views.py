from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound

from django.db.models import Q

from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django import forms
from django.urls import reverse_lazy
from .models import *
from .forms import *


class MainPage(LoginRequiredMixin, ListView):
    model = recipe
    template_name = 'main/index.html'
    login_url = reverse_lazy('welcome_page')
    raise_exception = False
    context_object_name = 'recipes'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class SearchResultsView(ListView):
    model = recipe
    template_name = 'recipe_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = recipe.objects.filter(Q(title_recipe__icontains=query))
        else:
            object_list = recipe.objects.all()
        return object_list

def welcomeDef(request):
    return render(request, 'main/welcome.html')

class AddRecipe(LoginRequiredMixin, CreateView):
    form_class = AddRecipeForm
    template_name = 'main/addrecipe.html'
    success_url = ''
    login_url = reverse_lazy('authorization_page')
    raise_exception = False

class AddProduct(LoginRequiredMixin, CreateView):
    form_class = AddProductForm
    template_name = 'main/addproduct.html'
    success_url = reverse_lazy('addrecipe_page')
    login_url = reverse_lazy('authorization_page')
    raise_exception = False

def errorDef(request):
    return render(request, 'main/404.html')

class AddFavRec(UpdateView):
    model = recipe
    template_name = 'main/AddFavRec.html'
    fields = ['fav_recs']

    def form_valid(self, form):
        user = self.request.user
        print(user)
        instance = form.save(commit=False)
        instance.save()
        print(instance)

        instance.fav_recs.set([user])

        instance.save()
        print(instance.fav_recs)

        return super().form_valid(form)

class profileDef(LoginRequiredMixin, CreateView):
    form_class = AddFavRecForm
    model = profile
    template_name = 'main/myprofile.html'
    login_url = reverse_lazy('authorization_page')
    success_url = reverse_lazy('profile_page')
    raise_exception = False

# def profileDef(request):
#     if request.method == 'POST':
#         form = AddFavRecForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             fav_rec = form.cleaned_data['favorite_recipes']
#             user.save()
#             user.favorite_recipes.set(fav_rec)
#             return redirect('myprofile.hmtl')
#     else:
#         form = AddFavRecForm()
#     return render( request,'main/myprofile.hmtl', {'form': form})

class ShowRecipe(DetailView):
    model = recipe
    template_name = 'main/recipe.html'
    slug_url_kwarg = 'recipe_slug'
    context_object_name = 'recipe'

class UpdRec(UpdateView):
    model = recipe
    template_name = 'main/addrecipe.html'
    form_class = AddRecipeForm

class DelRec(DeleteView):
    model = recipe
    success_url = reverse_lazy('house')
    template_name = 'main/deleterecipe.html'

def pageNotFound(request, exception):
    return render(request, 'main/404.html')

class RegisterUser(CreateView):
    form_class = UserForm
    template_name = 'main/registration.html'
    success_url = reverse_lazy('house')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('house')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('house')

def logout_user(request):
    logout(request)
    return redirect('authorization_page')