from django.urls import path

from .views import index, recipes_list, recipe_1, recipe_2, RecipeListView, RecipeDetailView

urlpatterns = [
    path('', index, name='index'),
    # path('recipes/list', recipes_list, name='recipes_list'),
    path('recipes/list', RecipeListView.as_view(), name='recipes_list'),
    # path('recipe/1', recipe_1, name='recipe_1'),
    # path('recipe/2', recipe_2, name='recipe_2'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe_<int:pk>')
]

app_name = "ledger"