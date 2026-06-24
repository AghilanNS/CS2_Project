from RestrauntData import *
import tkinter as tk
from tkinter import ttk


drivers = ["Mike", "Alex"]
delivery_records = []


def update_items(event=None):

    selected = type_var.get()

    item_box["values"] = [
        x.name
        for x in menu
        if x.category == selected
    ]


def update_items_delivery(event=None):

    selected = type_var2.get()

    item_box2["values"] = [
        x.name
        for x in menu
        if x.category == selected
    ]


def add_restaurant():

    selected_item = item_var.get()
    quantity = qty_var.get()

    chef = next(
        (
            s.name
            for s in staff_list
            if s.job == "Chef"
        ),
        "No Chef"
    )

    price = 0

    for item in menu:

        if item.name == selected_item:

            price = item.price * quantity

            break


    tree1.insert(
        "",
        "end",
        values=(
            table_var.get(),
            chef,
            selected_item,
            quantity,
            persons_var.get(),
            f"€{price:.2f}"
        )
    )


def clear_restaurant():

    for x in tree1.get_children():
        tree1.delete(x)


def add_delivery():

    selected_item = item_var2.get()
    quantity = qty_var2.get()

    chef = next(
        (
            s.name
            for s in staff_list
            if s.job == "Chef"
        ),
        "No Chef"
    )

    price = 0

    for item in menu:

        if item.name == selected_item:

            price = item.price * quantity

            break


    order = tree2.insert(
        "",
        "end",
        values=(
            driver_var.get(),
            address_var.get(),
            chef,
            selected_item,
            quantity,
            persons_var2.get(),
            f"€{price:.2f}"
        )
    )

    delivery_records.append(
        {
            "row": order,
            "item": selected_item,
            "qty": quantity,
            "delivered": False
        }
    )


def clear_delivery():

    for x in tree2.get_children():
        tree2.delete(x)


def load_kitchen():

    for item in menu:

        tree3.insert(
            "",
            "end",
            values=(
                item.name,
                1,
                "Chef",
                "Recipe",
                "-"
            )
        )


def clear_kitchen():

    for x in tree3.get_children():
        tree3.delete(x)

def deduct_inventory(item_name, quantity):

    for recipe in recipes:

        if recipe.recipe_name == item_name:

            for ingredient_name, amount in recipe.ingredients.items():

                ingredient = inventory.find_ingredient(
                    ingredient_name
                )

                if ingredient:

                    ingredient.use_stock(
                        amount * quantity
                    )


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


def reset_inventory():

    refresh_inventory()


def clear_inventory():

    for x in tree4.get_children():
        tree4.delete(x)

def mark_delivered():

    selected = tree2.selection()

    if not selected:
        return

    row = selected[0]

    values = tree2.item(
        row,
        "values"
    )

    item = values[3]

    qty = int(values[4])

    deduct_inventory(
        item,
        qty
    )

    new_values = list(values)

    new_values[-1] += " ✓"

    tree2.item(
        row,
        values=new_values
    )

def mark_paid():

    selected = tree2.selection()

    if not selected:
        return

    tree2.delete(
        selected[0]
    )


root = tk.Tk()
root.title("FINAL RESTAURANT SYSTEM")
root.geometry("1200x750")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

#PAGE 1
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

tk.Button(top1,text="ADD",command=add_restaurant).grid(row=0,column=5)
tk.Button(top1,text="CLEAR",command=clear_restaurant).grid(row=0,column=6)

tree1 = ttk.Treeview(
    page1,
    columns=("Table","Chef","Item","Qty","Persons","Price"),
    show="headings"
)

for c in tree1["columns"]:
    tree1.heading(c,text=c)

tree1.pack(fill="both",expand=True)


#PAGE 2
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
    text="PAID",
    command=mark_paid
).grid(row=0,column=8)

tree2=ttk.Treeview(
    page2,
    columns=("Driver","Address","Chef","Item","Qty","Persons","Price"),
    show="headings"
)

for c in tree2["columns"]:
    tree2.heading(c,text=c)

tree2.pack(fill="both",expand=True)

#PAGE 3
page3=ttk.Frame(notebook)
notebook.add(page3,text="Kitchen")

tk.Button(page3,text="LOAD",command=load_kitchen).pack()
tree3=ttk.Treeview(page3,columns=("Item","Qty","Chef","Recipe","Ingredients"),show="headings")

for c in tree3["columns"]:
    tree3.heading(c,text=c)

tree3.pack(fill="both",expand=True)

#PAGE 4
page4=ttk.Frame(notebook)
notebook.add(page4,text="Inventory")

tk.Button(page4,text="REFRESH",command=refresh_inventory).pack()

tree4=ttk.Treeview(page4,columns=("Ingredient","Stock"),show="headings")

for c in tree4["columns"]:
    tree4.heading(c,text=c)

tree4.pack(fill="both",expand=True)

root.mainloop()
