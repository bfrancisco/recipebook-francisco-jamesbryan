# run shell from manage.py, then type exec(open('recipe_parser.py').read())

from ledger.models import Recipe, Ingredient, RecipeIngredient


db = {
    "recipes": [
        {
            "name": "Sinigang",
            "author": "Gordon Ramsay",
            "ingredients": [
                {
                    "name": "tomato",
                    "quantity": "3pcs"
                },
                {
                    "name": "onion",
                    "quantity": "1pc"
                },
                {
                    "name": "pork",
                    "quantity": "1kg"
                },
                {
                    "name": "water",
                    "quantity": "1L"
                },
                {
                    "name": "sinigang mix",
                    "quantity": "1 packet"
                }
            ],
            "link": "/recipe/1"
        },
        {
            "name": "Adobo",
            "author": "Mom",
            "ingredients": [
                {
                    "name": "garlic",
                    "quantity": "1 head"
                },
                {
                    "name": "onion",
                    "quantity": "1pc"
                },
                {
                    "name": "vinegar",
                    "quantity": "1/2cup"
                },
                {
                    "name": "water",
                    "quantity": "1 cup"
                },
                {
                    "name": "salt",
                    "quantity": "1 tablespoon"
                },
                {
                    "name": "whole black peppers",
                    "quantity": "1 tablespoon"
                },
                {
                    "name": "pork",
                    "quantity": "1 kilo"
                }
            ],
            "link": "/recipe/2"
        }
    ]
}

for recipe in db['recipes']:
    reci_instance = Recipe()
    reci_instance.name = recipe['name']
    reci_instance.author = recipe['author']
    reci_instance.save()

    for ingredient in recipe['ingredients']:
        ingre_instance = Ingredient()
        ingre_instance.name = ingredient['name']

        rec_ing_instance = RecipeIngredient()
        rec_ing_instance.quantity = ingredient['quantity']
        rec_ing_instance.recipe = reci_instance
        rec_ing_instance.ingredient = ingre_instance

        ingre_instance.save()
        rec_ing_instance.save()

print("Done!")