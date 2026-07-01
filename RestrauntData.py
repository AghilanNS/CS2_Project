#Importing previously written classes
from Staff import Staff
from Delivery import Delivery
from Table import Table
from Menu_Item import MenuItem
from Ingredient import Ingredient
from Inventory import Inventory
from Recipe import Recipe

# Staff
staff_list = [
    Staff("Adam", "Chef"),
    Staff("Jason", "Chef"),
    Staff("Daniel", "Chef"),

    Staff("Emma", "Manager"),
    Staff("Lucas", "Bartender"),

    Staff("Mike", "Delivery Driver"),
    Staff("Alex", "Delivery Driver"),

    Staff("Sarah", "Waiter"),
    Staff("John", "Waiter"),
    Staff("Emily", "Waiter")
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
    MenuItem(5, "Chicken Burger", "Main Course", 9.50),
    MenuItem(6, "Vegetarian Burger", "Main Course", 8.50),
    MenuItem(7, "Cheeseburger", "Main Course", 10.50),
    MenuItem(8, "Pulled Pork Burger", "Main Course", 11.50),
    MenuItem(9, "Soft Drink", "Beverage", 2.50),
    MenuItem(10, "Iced Tea", "Beverage", 3.00),
    MenuItem(11, "Coffee", "Beverage", 3.00),
    MenuItem(12, "Beer", "Beverage", 4.50),
    MenuItem(13, "Fries", "Side", 3.50),
    MenuItem(14, "Sweet Potato Fries", "Side", 4.50),
    MenuItem(15, "Onion Rings", "Side", 4.00)
]




# Inventory
inventory = Inventory()
inventory.add_ingredient(Ingredient(1,"Pizza Dough",50,"pieces"))
inventory.add_ingredient(Ingredient(2,"Ham",30,"kg"))
inventory.add_ingredient(Ingredient(3,"Pepperoni",25,"kg"))
inventory.add_ingredient(Ingredient(4,"Chicken",40,"kg"))
inventory.add_ingredient(Ingredient(5,"Burger Buns",100,"pieces"))
inventory.add_ingredient(Ingredient(6,"Cheese",30,"kg"))
inventory.add_ingredient(Ingredient(7,"Tomato Sauce",25,"L"))
inventory.add_ingredient(Ingredient(8,"Tuna",20,"kg"))
inventory.add_ingredient(Ingredient(9,"Vegetables",40,"kg"))
inventory.add_ingredient(Ingredient(10,"Burger Patty",35,"kg"))
inventory.add_ingredient(Ingredient(11,"Pulled Pork",20,"kg"))
inventory.add_ingredient(Ingredient(12,"Lettuce",15,"kg"))
inventory.add_ingredient(Ingredient(13,"French Fries",50,"kg"))
inventory.add_ingredient(Ingredient(14,"Sweet Potato",40,"kg"))
inventory.add_ingredient(Ingredient(15,"Onion",30,"kg"))
inventory.add_ingredient(Ingredient(16,"Soft Drink Syrup",30,"L"))
inventory.add_ingredient(Ingredient(17,"Tea Leaves",10,"kg"))
inventory.add_ingredient(Ingredient(18,"Coffee Beans",20,"kg"))
inventory.add_ingredient(Ingredient(19,"Beer",100,"bottles"))
inventory.add_ingredient(Ingredient(20,"Ice",200,"pieces"))
inventory.add_ingredient(Ingredient(21,"Cooking Oil",50,"L"))
inventory.add_ingredient(Ingredient(22,"Veg Patty",40,"pieces"))
inventory.add_ingredient(Ingredient(23,"Beef Patty",40,"pieces"))

# Recipes

ham_pizza_recipe = Recipe("Ham Pizza")
ham_pizza_recipe.add_ingredient("Pizza Dough", 1)
ham_pizza_recipe.add_ingredient("Ham", 0.2)


pepperoni_pizza_recipe = Recipe("Pepperoni Pizza")
pepperoni_pizza_recipe.add_ingredient("Pizza Dough", 1)
pepperoni_pizza_recipe.add_ingredient("Pepperoni", 0.2)


tuna_pizza_recipe = Recipe("Tuna Pizza")
tuna_pizza_recipe.add_ingredient("Pizza Dough", 1)
tuna_pizza_recipe.add_ingredient("Tuna", 0.2)


vegetarian_pizza_recipe = Recipe("Vegetarian Pizza")
vegetarian_pizza_recipe.add_ingredient("Pizza Dough", 1)
vegetarian_pizza_recipe.add_ingredient("Vegetables", 0.3)


chicken_burger_recipe = Recipe("Chicken Burger")
chicken_burger_recipe.add_ingredient("Burger Buns", 1)
chicken_burger_recipe.add_ingredient("Chicken", 0.2)


vegetarian_burger_recipe = Recipe("Vegetarian Burger")
vegetarian_burger_recipe.add_ingredient("Burger Buns", 1)
vegetarian_burger_recipe.add_ingredient("Veg Patty", 1)


cheeseburger_recipe = Recipe("Cheeseburger")
cheeseburger_recipe.add_ingredient("Burger Buns", 1)
cheeseburger_recipe.add_ingredient("Beef Patty", 1)
cheeseburger_recipe.add_ingredient("Cheese", 1)


pulled_pork_recipe = Recipe("Pulled Pork Burger")
pulled_pork_recipe.add_ingredient("Burger Buns", 1)
pulled_pork_recipe.add_ingredient("Pulled Pork", 0.2)

fries_recipe = Recipe("Fries Recipe")
fries_recipe.add_ingredient("French Fries",1)
fries_recipe.add_ingredient("Cooking Oil",0.2)

sweet_fries_recipe = Recipe("Sweet Potato Fries Recipe")
sweet_fries_recipe.add_ingredient("Sweet Potato",1)
sweet_fries_recipe.add_ingredient("Cooking Oil",0.2)

onion_recipe = Recipe("Onion Rings Recipe")
onion_recipe.add_ingredient("Onion",0.5)
onion_recipe.add_ingredient("Cooking Oil",0.2)

soft_recipe = Recipe("Soft Drink Recipe")
soft_recipe.add_ingredient("Soft Drink Syrup",0.3)
soft_recipe.add_ingredient("Ice",5)

tea_recipe = Recipe("Iced Tea Recipe")
tea_recipe.add_ingredient("Tea Leaves",0.1)
tea_recipe.add_ingredient("Ice",5)

coffee_recipe = Recipe("Coffee Recipe")
coffee_recipe.add_ingredient("Coffee Beans",0.1)

beer_recipe = Recipe("Beer Recipe")
beer_recipe.add_ingredient("Beer",1)

#Recipe List
recipes = [
    ham_pizza_recipe,
    pepperoni_pizza_recipe,
    tuna_pizza_recipe,
    vegetarian_pizza_recipe,

    chicken_burger_recipe,
    vegetarian_burger_recipe,
    cheeseburger_recipe,
    pulled_pork_recipe,

    fries_recipe,
    sweet_fries_recipe,
    onion_recipe,

    soft_recipe,
    tea_recipe,
    coffee_recipe,
    beer_recipe
]

#Menu
menu[0].recipe = ham_pizza_recipe
menu[1].recipe = pepperoni_pizza_recipe
menu[2].recipe = tuna_pizza_recipe
menu[3].recipe = vegetarian_pizza_recipe
menu[4].recipe = chicken_burger_recipe
menu[5].recipe = vegetarian_burger_recipe
menu[6].recipe = cheeseburger_recipe
menu[7].recipe = pulled_pork_recipe

menu[8].recipe = soft_recipe
menu[9].recipe = tea_recipe
menu[10].recipe = coffee_recipe
menu[11].recipe = beer_recipe

menu[12].recipe = fries_recipe
menu[13].recipe = sweet_fries_recipe
menu[14].recipe = onion_recipe

# Default Inventory Stock
default_inventory = {}

for ingredient in inventory.ingredients:

    default_inventory[
        ingredient.name
    ] = ingredient.quantity_in_stock
