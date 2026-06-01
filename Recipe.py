class Recipe:
    def __init__(self, recipe_name):
        self.recipe_name = recipe_name
        self.ingredients = {}

    def add_ingredient(self, ingredient, quantity):
        self.ingredients[ingredient] = quantity

    def display_recipe(self):
        recipe_text = f"Recipe: {self.recipe_name}\n"

        for ingredient, quantity in self.ingredients.items():
            recipe_text += (
                f"{ingredient.name}: "
                f"{quantity} {ingredient.unit}\n"
            )

        return recipe_text