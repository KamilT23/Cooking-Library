from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPage.as_view(), name='house'),
    path('search', SearchResultsView.as_view(), name='search_results'),
    path('welcome', welcomeDef, name='welcome_page'),
    path('registration', RegisterUser.as_view(), name='registration_page'),
    path('login', LoginUser.as_view(), name='authorization_page'),
    path('logout', logout_user, name='exit_page'),
    path('addrecipe', AddRecipe.as_view(), name='addrecipe_page'),
    path('addproduct', AddProduct.as_view(), name='addproduct_page'),
    path('recipe/<slug>/favourite', AddFavRec.as_view(), name='add_favourite'),
    path('error', errorDef, name='error_page'),
    path('profile', profileDef.as_view(), name='profile_page'),
    path('recipe/<slug:recipe_slug>', ShowRecipe.as_view(), name='recipe'),
    path('recipe/<slug>/update', UpdRec.as_view(),name='update_recipe'),
    path('recipe/<slug>/delete', DelRec.as_view(),name='delete_recipe'),
]