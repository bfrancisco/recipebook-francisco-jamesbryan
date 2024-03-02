from django.contrib import admin

from .models import Recipe, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline,]

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    list_display = ['ingredient', 'quantity', 'recipe']
    search_fields = ['ingredient', 'quantity', 'recipe']
    list_filter = ['recipe']

    fieldsets = [
        ('Details', {
            'fields' : [
                ('ingredient', 'quantity', 'recipe')
            ]
        })
    ]
    
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
