#Aghilan
#Defining class Ingredient
class Ingredient:
    def __init__(self, ingredient_id, name, quantity_in_stock, unit):
        self.ingredient_id = ingredient_id
        self.name = name
        self.quantity_in_stock = quantity_in_stock
        self.unit = unit

    def add_stock(self, amount):
        self.quantity_in_stock += amount

    def use_stock(self, amount):
        if amount <= self.quantity_in_stock:
            self.quantity_in_stock -= amount
        else:
            print("Not enough stock available.")

    def display_info(self):
        return (
            f"Ingredient ID: {self.ingredient_id}\n"
            f"Name: {self.name}\n"
            f"Stock: {self.quantity_in_stock} {self.unit}"
        )