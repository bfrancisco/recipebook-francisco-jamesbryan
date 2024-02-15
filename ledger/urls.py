from django.urls import path

from .views import index, recipe_list, recipe_1, recipe_2

urlpatterns = [
    path('', index, name='index'),
    path('recipes/list', recipe_list, name='recipes'),
    path('recipe/1', recipe_1, name='recipes'),
    path('recipe/2', recipe_2, name='recipes'),
]

app_name = "ledger"