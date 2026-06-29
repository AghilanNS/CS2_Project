#Import previously written classes
#Import previously assigned data
from RestrauntData import *
import tkinter as tk
from tkinter import ttk


drivers = ["Mike", "Alex"]
waiter_index = 0
delivery_records = []
kitchen_orders = []
chef_index = 0

def update_items(event=None):

    selected = type_var.get()

    item_box["values"] = [
        x.name
        for x in menu
        if x.category == selected
    ]

#Ad Orders(Delivery)
def update_items_delivery(event=None):

    selected = type_var2.get()

    item_box2["values"] = [
        x.name
        for x in menu
        if x.category == selected
    ]

#Add Orders(Dine-in)
def add_restaurant():

    global waiter_index

    selected_item = item_var.get()
    quantity = qty_var.get()

    waiters = [
        s.name
        for s in staff_list
        if s.job == "Waiter"
    ]

    waiter = waiters[
        waiter_index % len(waiters)
    ]

    waiter_index += 1


    price = 0
    selected_recipe = None


    for item in menu:

        if item.name == selected_item:

            price = item.price * quantity

            if hasattr(item, "recipe"):

                selected_recipe = item.recipe

            break


    tree1.insert(
        "",
        "end",
        values=(
            table_var.get(),
            waiter,
            selected_item,
            quantity,
            persons_var.get(),
            f"€{price:.2f}"
        )
    )


    kitchen_orders.append(
        (
            selected_item,
            quantity,
            selected_recipe
        )
    )


def clear_restaurant():

    for x in tree1.get_children():
        tree1.delete(x)


def add_delivery():

    selected_item = item_var2.get()
    quantity = qty_var2.get()

    price = 0
    selected_recipe = None


    for item in menu:

        if item.name == selected_item:

            price = item.price * quantity

            if hasattr(item,"recipe"):

                selected_recipe = item.recipe

            break


    tree2.insert(
        "",
        "end",
        values=(
            driver_var.get(),
            address_var.get(),
            selected_item,
            quantity,
            f"€{price:.2f}"
        )
    )


    kitchen_orders.append(
        (
            selected_item,
            quantity,
            selected_recipe
        )
    )


def clear_delivery():

    for x in tree2.get_children():
        tree2.delete(x)

#Update all ongoing orders in Kitchen page
def load_kitchen():

    global chef_index

    tree3.delete(*tree3.get_children())

    chefs = [
        s.name
        for s in staff_list
        if s.job == "Chef"
    ]

    bartenders = [
        s.name
        for s in staff_list
        if s.job == "Bartender"
    ]


    for order in kitchen_orders:

        item_name = order[0]
        quantity = order[1]
        recipe = order[2]


        assigned = "Unassigned"


        for item in menu:

            if item.name == item_name:

                if item.category == "Beverage":

                    if bartenders:
                        assigned = bartenders[0]

                else:

                    assigned = chefs[
                        chef_index % len(chefs)
                    ]

                    chef_index += 1

                break


        recipe_name = "-"
        ingredients = "-"


        if recipe:

            recipe_name = recipe.recipe_name

            ingredients = ", ".join(
                recipe.ingredients.keys()
            )


        tree3.insert(
            "",
            "end",
            values=(
                item_name,
                quantity,
                assigned,
                recipe_name,
                ingredients
            )
        )
        
        
def deduct_inventory(item_name, quantity):

    for item in menu:

        if item.name == item_name:

            if hasattr(item, "recipe"):

                recipe = item.recipe


                for ingredient_name, amount in recipe.ingredients.items():

                    for ingredient in inventory.ingredients:

                        if ingredient.name == ingredient_name:

                            ingredient.quantity_in_stock -= (
                                amount * quantity
                            )

                            if ingredient.quantity_in_stock < 0:

                                ingredient.quantity_in_stock = 0

            break
        
#Send out order from Kitchen        
def send_kitchen_order():

    selected = tree3.selection()

    if not selected:
        return


    for row in selected:

        values = tree3.item(
            row,
            "values"
        )

        item_name = values[0]
        quantity = int(values[1])


        deduct_inventory(
            item_name,
            quantity
        )


        for i, order in enumerate(kitchen_orders):

            if (
                order[0] == item_name
                and order[1] == quantity
            ):

                kitchen_orders.pop(i)

                break


        tree3.delete(row)


    refresh_inventory()

#Clear orders
def clear_kitchen():

    for x in tree3.get_children():
        tree3.delete(x)

#Deduction after order sent out
def deduct_inventory(item_name, quantity):

    recipe_found = None


    for recipe in recipes:

        recipe_name = (
            recipe.recipe_name
            .replace(" Recipe","")
        )

        if recipe_name == item_name:

            recipe_found = recipe

            break


    if recipe_found:

        for ingredient_name, amount in recipe_found.ingredients.items():

            for ingredient in inventory.ingredients:

                if (
                    ingredient.name
                    == ingredient_name
                ):

                    ingredient.quantity_in_stock -= (
                        amount * quantity
                    )


                    if (
                        ingredient.quantity_in_stock
                        < 0
                    ):

                        ingredient.quantity_in_stock = 0

#Update Inventory
def refresh_inventory():

    clear_inventory()

    for i in inventory.ingredients:

        tree4.insert(
            "",
            "end",
            values=(
                i.name,
                f"{i.quantity_in_stock} {i.unit}"
            )
        )

#Reset stock to original value
def reset_inventory():

    for ingredient in inventory.ingredients:

        if ingredient.name in default_inventory:

            ingredient.quantity_in_stock = (
                default_inventory[
                    ingredient.name
                ]
            )

    refresh_inventory()


def clear_inventory():

    for x in tree4.get_children():
        tree4.delete(x)

#Delivery Status
def mark_delivered():

    selected = tree2.selection()

    if not selected:
        return


    for row in selected:

        tree2.delete(row)

#Payment Status
def mark_paid():

    selected = tree2.selection()

    if not selected:
        return

    tree2.delete(
        selected[0]
    )

def mark_paid_restaurant():

    selected = tree1.selection()

    if not selected:
        return

    tree1.delete(
        selected[0]
    )


root = tk.Tk()
root.title("FINAL RESTAURANT SYSTEM")
root.geometry("1200x750")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

#Onur
#Designing Page 1
page1 = ttk.Frame(notebook)
notebook.add(page1, text="Restaurant")

top1 = ttk.Frame(page1)
top1.pack(fill="x")

type_var = tk.StringVar()
table_var = tk.StringVar()
item_var = tk.StringVar()
qty_var = tk.IntVar(value=1)
persons_var = tk.IntVar(value=1)

type_box = ttk.Combobox(
    top1,
    textvariable=type_var,
    values=["Main Course", "Beverage", "Side"]
)

type_box.grid(row=0,column=0)
type_box.bind("<<ComboboxSelected>>", update_items)

item_box = ttk.Combobox(top1,textvariable=item_var)
item_box.grid(row=0,column=1)

ttk.Combobox(
    top1,
    textvariable=table_var,
    values=[f"T{i}" for i in range(1,11)]
).grid(row=0,column=2)

tk.Spinbox(top1,from_=1,to=10,textvariable=qty_var).grid(row=0,column=3)
tk.Spinbox(top1,from_=1,to=10,textvariable=persons_var).grid(row=0,column=4)

tk.Button(
    top1,
    text="ADD",
    command=add_restaurant
).grid(row=0,column=5)

tk.Button(
    top1,
    text="PAID",
    command=mark_paid_restaurant
).grid(row=0,column=6)

tk.Button(
    top1,
    text="CLEAR",
    command=clear_restaurant
).grid(row=0,column=7)

tree1 = ttk.Treeview(
    page1,
    columns=("Table","Waiter","Item","Qty","Persons","Price"),
    show="headings"
)

for c in tree1["columns"]:
    tree1.heading(c,text=c)

tree1.pack(fill="both",expand=True)

#Aghilan
#Designing Page 2
page2 = ttk.Frame(notebook)
notebook.add(page2,text="Delivery")

top2 = ttk.Frame(page2)
top2.pack(fill="x")

driver_var=tk.StringVar()
address_var=tk.StringVar()
item_var2=tk.StringVar()
qty_var2=tk.IntVar(value=1)
persons_var2=tk.IntVar(value=1)
type_var2=tk.StringVar()

ttk.Combobox(top2,textvariable=driver_var,values=drivers).grid(row=0,column=0)

tk.Entry(top2,textvariable=address_var).grid(row=0,column=1)

type_box2=ttk.Combobox(
    top2,
    textvariable=type_var2,
    values=["Main Course","Beverage","Side"]
)

type_box2.grid(row=0,column=2)

item_box2=ttk.Combobox(top2,textvariable=item_var2)
item_box2.grid(row=0,column=3)

type_box2.bind(
    "<<ComboboxSelected>>",
    update_items_delivery
)

tk.Spinbox(top2,from_=1,to=10,textvariable=qty_var2).grid(row=0,column=4)

tk.Button(
    top2,
    text="ADD",
    command=add_delivery
).grid(row=0,column=6)

tk.Button(
    top2,
    text="DELIVERED",
    command=mark_delivered
).grid(row=0,column=7)

tk.Button(
    top2,
    text="CLEAR",
    command=clear_delivery
).grid(row=0,column=8)

tree2 = ttk.Treeview(
    page2,
    columns=(
        "Driver",
        "Address",
        "Item",
        "Qty",
        "Price"
    ),
    show="headings"
)

for c in tree2["columns"]:
    tree2.heading(c,text=c)

tree2.pack(
    fill="both",
    expand=True
)

for c in tree2["columns"]:
    tree2.heading(c,text=c)

tree2.pack(fill="both",expand=True)


#Aghilan
#Designing Page 3
page3 = ttk.Frame(notebook)
notebook.add(page3,text="Kitchen")

tk.Button(
    page3,
    text="LOAD",
    command=load_kitchen
).pack()

tk.Button(
    page3,
    text="SENT OUT",
    command=send_kitchen_order
).pack()

tk.Button(
    page3,
    text="CLEAR",
    command=clear_kitchen
).pack()


tree3 = ttk.Treeview(
page3,
columns=(
"Item",
"Qty",
"Chef",
"Ingredients"
),
show="headings"
)


for c in tree3["columns"]:
    tree3.heading(c,text=c)

tree3.pack(
    fill="both",
    expand=True
)

#Onur
#Designing Page 4
page4=ttk.Frame(notebook)
notebook.add(page4,text="Inventory")

tk.Button(page4,text="REFRESH",command=refresh_inventory).pack()
tk.Button(page4,text="RESET",command=reset_inventory).pack()

tree4=ttk.Treeview(page4,columns=("Ingredient","Stock"),show="headings")

for c in tree4["columns"]:
    tree4.heading(c,text=c)

tree4.pack(fill="both",expand=True)

root.mainloop()