#Onur
#Defining class Inventory
class Inventory:
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def find_ingredient(self, ingredient_name):
        for ingredient in self.ingredients:
            if ingredient.name == ingredient_name:
                return ingredient

        return None

    def show_inventory(self):
        inventory_text = "Current Inventory:\n\n"

        for ingredient in self.ingredients:
            inventory_text += (ingredient.display_info() + "\n\n")

        return inventory_text