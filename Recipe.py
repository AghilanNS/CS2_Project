#Aghilan
#Defining class Recipe
class Recipe:

    def __init__(self, recipe_name):
        self.recipe_name = recipe_name
        self.ingredients = {}

    def add_ingredient(self, ingredient_name, quantity):
        self.ingredients[ingredient_name] = quantity

    def display_recipe(self):

        recipe_text = f"{self.recipe_name}\n"

        for ingredient, quantity in self.ingredients.items():
            recipe_text += f"{ingredient}: {quantity}\n"

        return recipe_text