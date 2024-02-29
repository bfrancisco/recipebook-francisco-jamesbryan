from django.db import models
from django.urls import reverse


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'[INGREDIENT] {self.name}'

    # set url
    
class Recipe(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'[RECIPE] {self.name}'

    # not sure
    def get_absolute_url(self):
        return reverse(f'/recipe/{self.pk}', args=[str(self.pk)])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(
        'Ingredient',
        on_delete=models.CASCADE, 
        default=0, 
        related_name='ingredients'
    )
    recipe = models.ForeignKey(
        'Recipe',
        on_delete=models.CASCADE, 
        default=0, 
        related_name='recipe'
    )

    
