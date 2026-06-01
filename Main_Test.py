#Testing all written classes at once
#Inporting all previous classes
from Staff import Staff
from Delivery import Delivery
from Table import Table
from Menu_Item_Combined import MenuItem
from Order import Order
from Ingredient import Ingredient
from Recipe import Recipe
from Inventory import Inventory

#Testing Staff Class
print("\nStaff Test")
staff1 = Staff("John", "Waiter")
staff2 = Staff("Sarah", "Chef")
print(staff1.display_info())
print()
print(staff2.display_info())

#Testing Delivery Class
print("\nDelivery Test")
delivery1 = Delivery("Mike","12 Bahnhof Street",101)
print(delivery1.display_info())

#Testing Table Class
print("\nTable Test")
table1 = Table(5, 4)
table1.add_to_bill(25.00)
table1.add_to_bill(12.50)
print(table1.display_info())
table1.make_payment()
print("\nAfter Payment:")
print(table1.display_info())

#Testing Menu Item Class
print("\nMenu Item Test")
burger = MenuItem(1,"Burger","Main Course",8.50,cooked_level="Medium")
cola = MenuItem(2,"Cola","Beverage",2.50,temperature="Cold",with_ice="Yes")
fries = MenuItem(3,"Fries","Side",3.00)

print(burger.display_info())
print()
print(cola.display_info())
print()
print(fries.display_info())

#Testing Order Class
print("\nOrder Test")
order1 = Order(101, "Dine-In")
order1.add_item(burger)
order1.add_item(cola)
order1.add_item(fries)
print(order1.display_info())

#Testing Ingredient Class
print("\nIngredient Test")
potato = Ingredient(1,"Potato",100,"pieces")
beef = Ingredient(2,"Beef Patty",50,"pieces")
print(potato.display_info())
print()
print(beef.display_info())

#Testing Recipe Class
print("\nRecipe Test")
burger_recipe = Recipe("Burger")
burger_recipe.add_ingredient(beef, 1)
burger_recipe.add_ingredient(potato, 2)
print(burger_recipe.display_recipe())

#Testing Inventory Class
print("\nInventory Test")
inventory = Inventory()
inventory.add_ingredient(potato)
inventory.add_ingredient(beef)
print(inventory.show_inventory())