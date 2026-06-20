from staff import Staff
from delivery import Delivery
from table import Table
from menu_item import MenuItem
from ingredient import Ingredient
from inventory import Inventory
from recipe import Recipe

# Staff
staff_list = [
    Staff("Adam", "Chef"),
    Staff("Jason", "Chef"),
    Staff("Daniel", "Chef"),
    Staff("Emma", "Cashier"),
    Staff("Mike", "Delivery Driver"),
    Staff("Alex", "Delivery Driver")
]


# Delivery Motorbikes
delivery_motorbikes = {
    "Mike": ["MB101", "MB102"],
    "Alex": ["MB201", "MB202"]
}


# Tables
tables = [
    Table(1, 2),
    Table(2, 2),
    Table(3, 4),
    Table(4, 4),
    Table(5, 4),
    Table(6, 4),
    Table(7, 6),
    Table(8, 6),
    Table(9, 8),
    Table(10, 8)
]


# Menu Items
menu = [
    MenuItem(1, "Ham Pizza", "Main Course", 12.50),
    MenuItem(2, "Pepperoni Pizza", "Main Course", 13.50),
    MenuItem(3, "Tuna Pizza", "Main Course", 13.00),
    MenuItem(4, "Vegetarian Pizza", "Main Course", 11.50),
    MenuItem(5, "Chicken Burger", "Main Course", 9.50, cooked_level="Well Done"),
    MenuItem(6, "Vegetarian Burger", "Main Course", 8.50),
    MenuItem(7, "Cheeseburger", "Main Course", 10.50, cooked_level="Medium"),
    MenuItem(8, "Pulled Pork Burger", "Main Course", 11.50, cooked_level="Well Done"),
    MenuItem(9, "Soft Drink", "Beverage", 2.50, temperature="Cold", with_ice="Yes"),
    MenuItem(10, "Iced Tea", "Beverage", 3.00, temperature="Cold", with_ice="No"),
    MenuItem(11, "Coffee", "Beverage", 3.00, temperature="Hot"),
    MenuItem(12, "Beer", "Beverage", 4.50, temperature="Cold", with_ice="No"),
    MenuItem(13, "Fries", "Side", 3.50),
    MenuItem(14, "Sweet Potato Fries", "Side", 4.50),
    MenuItem(15, "Onion Rings", "Side", 4.00)
]


# Delivery
delivery_1 = Delivery("Mike", "12 Bahnhof Street", 101)


# Inventory
inventory = Inventory()
inventory.add_ingredient(Ingredient(1, "Pizza Dough", 50, "pieces"))
inventory.add_ingredient(Ingredient(2, "Ham", 30, "kg"))
inventory.add_ingredient(Ingredient(3, "Pepperoni", 25, "kg"))
inventory.add_ingredient(Ingredient(4, "Chicken", 40, "kg"))
inventory.add_ingredient(Ingredient(5, "Burger Buns", 100, "pieces"))
inventory.add_ingredient(Ingredient(6, "Tuna", 20, "kg"))
inventory.add_ingredient(Ingredient(7, "Vegetables", 35, "kg"))
inventory.add_ingredient(Ingredient(8, "Veg Patty", 40, "pieces"))
inventory.add_ingredient(Ingredient(9, "Beef Patty", 60, "pieces"))
inventory.add_ingredient(Ingredient(10, "Cheese", 150, "slices"))
inventory.add_ingredient(Ingredient(11, "Pulled Pork", 25, "kg"))

# Recipes
ham_pizza_recipe = Recipe("Ham Pizza")
ham_pizza_recipe.add_ingredient(Ingredient(1, "Pizza Dough", 1, "piece"))
ham_pizza_recipe.add_ingredient(Ingredient(2, "Ham", 0.2, "kg"))

pepperoni_pizza_recipe = Recipe("Pepperoni Pizza")
pepperoni_pizza_recipe.add_ingredient(Ingredient(1, "Pizza Dough", 1, "piece"))
pepperoni_pizza_recipe.add_ingredient(Ingredient(3, "Pepperoni", 0.2, "kg"))

tuna_pizza_recipe = Recipe("Tuna Pizza")
tuna_pizza_recipe.add_ingredient(Ingredient(1, "Pizza Dough", 1, "piece"))
tuna_pizza_recipe.add_ingredient(Ingredient(6, "Tuna", 0.2, "kg"))

vegetarian_pizza_recipe = Recipe("Vegetarian Pizza")
vegetarian_pizza_recipe.add_ingredient(Ingredient(1, "Pizza Dough", 1, "piece"))
vegetarian_pizza_recipe.add_ingredient(Ingredient(7, "Vegetables", 0.3, "kg"))

chicken_burger_recipe = Recipe("Chicken Burger")
chicken_burger_recipe.add_ingredient(Ingredient(5, "Burger Buns", 1, "piece"))
chicken_burger_recipe.add_ingredient(Ingredient(4, "Chicken", 0.2, "kg"))

vegetarian_burger_recipe = Recipe("Vegetarian Burger")
vegetarian_burger_recipe.add_ingredient(Ingredient(5, "Burger Buns", 1, "piece"))
vegetarian_burger_recipe.add_ingredient(Ingredient(8, "Veg Patty", 1, "piece"))

cheeseburger_recipe = Recipe("Cheeseburger")
cheeseburger_recipe.add_ingredient(Ingredient(5, "Burger Buns", 1, "piece"))
cheeseburger_recipe.add_ingredient(Ingredient(9, "Beef Patty", 1, "piece"))
cheeseburger_recipe.add_ingredient(Ingredient(10, "Cheese", 1, "slice"))

pulled_pork_recipe = Recipe("Pulled Pork Burger")
pulled_pork_recipe.add_ingredient(Ingredient(5, "Burger Buns", 1, "piece"))
pulled_pork_recipe.add_ingredient(Ingredient(11, "Pulled Pork", 0.2, "kg"))

#Recipe List
recipes = [ham_pizza_recipe,pepperoni_pizza_recipe,tuna_pizza_recipe,vegetarian_pizza_recipe,chicken_burger_recipe,vegetarian_burger_recipe,cheeseburger_recipe,pulled_pork_recipe]