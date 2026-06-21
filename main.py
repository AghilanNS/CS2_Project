import tkinter as tk
from tkinter import ttk, messagebox

# ===================== INGREDIENT =====================

class Ingredient:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock
        self.initial = stock

    def use(self, amount):
        if self.stock - amount < 0:
            return False
        self.stock -= amount
        return True

    def reset(self):
        self.stock = self.initial


# ===================== MENU ITEM =====================

class MenuItem:
    def __init__(self, name, type_, price, chef, ingredients, recipe):
        self.name = name
        self.type = type_
        self.price = price
        self.chef = chef
        self.ingredients = ingredients
        self.recipe = recipe


# ===================== DATA =====================

waiters = ["Joe", "Jonathan", "Lisa"]
drivers = ["Stefan", "Holger", "Linda"]
chefs = ["Maria", "Jack", "Adam"]

ingredients = {
    "meat": Ingredient("meat", 30),
    "bread": Ingredient("bread", 30),
    "tomato": Ingredient("tomato", 30),
    "dough": Ingredient("dough", 30),
    "potato": Ingredient("potato", 30),
    "onion": Ingredient("onion", 30),
    "cola": Ingredient("cola", 30),
}

menu = {
    "Beverage": {
        "Water": MenuItem("Water","Beverage",2,None,{}, "-"),
        "Cola": MenuItem("Cola","Beverage",3,None,{"cola":1},"Cold drink"),
        "Fanta": MenuItem("Fanta","Beverage",3,None,{"cola":1},"Orange drink")
    },

    "Meal": {
        "Burger": MenuItem("Burger","Meal",10,"Maria",
                           {"meat":1,"bread":2,"tomato":1},
                           "Grill + assemble"),

        "Pizza": MenuItem("Pizza","Meal",12,"Jack",
                           {"dough":2,"meat":1,"tomato":1},
                           "Bake in oven"),

        "Doner": MenuItem("Doner","Meal",11,"Adam",
                           {"meat":1,"bread":1,"tomato":1},
                           "Wrap + grill")
    },

    "Side": {
        "Potato": MenuItem("Potato","Side",5,"Maria",
                           {"potato":1},
                           "Fry potatoes"),

        "Onion Ring": MenuItem("Onion Ring","Side",6,"Jack",
                               {"onion":1},
                               "Fry onion rings")
    }
}

restaurant_orders = []
delivery_orders = []

# ===================== INGREDIENT SYSTEM =====================

def apply_ingredients(item, qty):
    for cat in menu.values():
        if item in cat:
            m = cat[item]
            for ing, amount in m.ingredients.items():
                if ing in ingredients:
                    ingredients[ing].use(amount * qty)
            return


# ===================== RESTAURANT =====================

def update_items(event=None):
    t = type_var.get()
    item_box["values"] = list(menu[t].keys())
    item_var.set("Select Item")


def add_restaurant():
    item = item_var.get()
    table = table_var.get()
    qty = qty_var.get()
    persons = persons_var.get()
    type_ = type_var.get()

    if item == "Select Item":
        return

    m = menu[type_][item]
    price = m.price * qty * persons

    apply_ingredients(item, qty * persons)

    restaurant_orders.append((item, qty * persons, m.chef, m.recipe, m.ingredients))

    tree1.insert("", "end", values=(
        table,
        m.chef,
        item,
        qty,
        persons,
        price
    ))


def clear_restaurant():
    tree1.delete(*tree1.get_children())
    restaurant_orders.clear()


# ===================== DELIVERY =====================

def update_items_delivery(event=None):
    t = type_var2.get()
    item_box2["values"] = list(menu[t].keys())
    item_var2.set("Select Item")


def add_delivery():
    driver = driver_var.get()
    address = address_var.get()
    item = item_var2.get()
    qty = qty_var2.get()
    persons = persons_var2.get()
    type_ = type_var2.get()

    if item == "Select Item":
        return

    m = menu[type_][item]
    price = m.price * qty * persons

    apply_ingredients(item, qty * persons)

    delivery_orders.append((item, qty * persons, m.chef, m.recipe, m.ingredients))

    tree2.insert("", "end", values=(
        driver,
        address,
        m.chef,
        item,
        qty,
        persons,
        price
    ))


def clear_delivery():
    tree2.delete(*tree2.get_children())
    delivery_orders.clear()


# ===================== KITCHEN =====================

def load_kitchen():
    tree3.delete(*tree3.get_children())

    totals = {}

    for item, qty, chef, recipe, ing in restaurant_orders + delivery_orders:
        if item not in totals:
            totals[item] = {
                "qty":0,
                "chef":chef,
                "recipe":recipe,
                "ing":ing
            }
        totals[item]["qty"] += qty

    for item, data in totals.items():

        tree3.insert("", "end", values=(
            item,
            data["qty"],
            data["chef"],
            data["recipe"],
            data["ing"]
        ))


def clear_kitchen():
    tree3.delete(*tree3.get_children())


# ===================== INVENTORY =====================

def refresh_inventory():
    tree4.delete(*tree4.get_children())
    for ing in ingredients.values():
        tree4.insert("", "end", values=(ing.name, ing.stock))


def reset_inventory():
    for ing in ingredients.values():
        ing.reset()
    refresh_inventory()
    messagebox.showinfo("Inventory","Reset Done")


def clear_inventory():
    tree4.delete(*tree4.get_children())


# ===================== UI =====================

root = tk.Tk()
root.title("FINAL RESTAURANT SYSTEM")
root.geometry("1200x750")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# ===================== PAGE 1 =====================

page1 = ttk.Frame(notebook)
notebook.add(page1, text="Restaurant")

top1 = ttk.Frame(page1)
top1.pack(fill="x")

type_var = tk.StringVar()
table_var = tk.StringVar()
item_var = tk.StringVar()
qty_var = tk.IntVar(value=1)
persons_var = tk.IntVar(value=1)

ttk.Combobox(top1,textvariable=type_var,
             values=list(menu.keys())).grid(row=0,column=0)

type_box = top1.children[list(top1.children)[0]]
type_box.bind("<<ComboboxSelected>>", update_items)

item_box = ttk.Combobox(top1,textvariable=item_var)
item_box.set("Select Item")
item_box.grid(row=0,column=1)

ttk.Combobox(top1,textvariable=table_var,
             values=["T1","T2","T3"]).grid(row=0,column=2)

tk.Spinbox(top1,from_=1,to=10,textvariable=qty_var).grid(row=0,column=3)
tk.Spinbox(top1,from_=1,to=10,textvariable=persons_var).grid(row=0,column=4)

tk.Button(top1,text="ADD",command=add_restaurant).grid(row=0,column=5)
tk.Button(top1,text="CLEAR",command=clear_restaurant).grid(row=0,column=6)

tree1 = ttk.Treeview(page1,
columns=("Table","Chef","Item","Qty","Persons","Price"),
show="headings")

for c in tree1["columns"]:
    tree1.heading(c,text=c)

tree1.pack(fill="both",expand=True)


# ===================== PAGE 2 =====================

page2 = ttk.Frame(notebook)
notebook.add(page2,text="Delivery")

top2 = ttk.Frame(page2)
top2.pack(fill="x")

driver_var = tk.StringVar()
address_var = tk.StringVar()
item_var2 = tk.StringVar()
qty_var2 = tk.IntVar(value=1)
persons_var2 = tk.IntVar(value=1)
type_var2 = tk.StringVar()

ttk.Combobox(top2,textvariable=driver_var,
             values=drivers).grid(row=0,column=0)

tk.Entry(top2,textvariable=address_var).grid(row=0,column=1)

ttk.Combobox(top2,textvariable=type_var2,
             values=list(menu.keys())).grid(row=0,column=2)

item_box2 = ttk.Combobox(top2,textvariable=item_var2)
item_box2.set("Select Item")
item_box2.grid(row=0,column=3)

type_box2 = top2.children[list(top2.children)[2]]
type_box2.bind("<<ComboboxSelected>>", update_items_delivery)

tk.Spinbox(top2,from_=1,to=10,textvariable=qty_var2).grid(row=0,column=4)
tk.Spinbox(top2,from_=1,to=10,textvariable=persons_var2).grid(row=0,column=5)

tk.Button(top2,text="ADD",command=add_delivery).grid(row=0,column=6)
tk.Button(top2,text="CLEAR",command=clear_delivery).grid(row=0,column=7)

tree2 = ttk.Treeview(page2,
columns=("Driver","Address","Chef","Item","Qty","Persons","Price"),
show="headings")

for c in tree2["columns"]:
    tree2.heading(c,text=c)

tree2.pack(fill="both",expand=True)


# ===================== PAGE 3 =====================

page3 = ttk.Frame(notebook)
notebook.add(page3,text="Kitchen")

tk.Button(page3,text="LOAD",command=load_kitchen).pack()
tk.Button(page3,text="CLEAR",command=clear_kitchen).pack()

tree3 = ttk.Treeview(page3,
columns=("Item","Qty","Chef","Recipe","Ingredients"),
show="headings")

for c in tree3["columns"]:
    tree3.heading(c,text=c)

tree3.pack(fill="both",expand=True)


# ===================== PAGE 4 =====================

page4 = ttk.Frame(notebook)
notebook.add(page4,text="Inventory")

tk.Button(page4,text="RESET",command=reset_inventory).pack()
tk.Button(page4,text="REFRESH",command=refresh_inventory).pack()
tk.Button(page4,text="CLEAR",command=clear_inventory).pack()

tree4 = ttk.Treeview(page4,
columns=("Ingredient","Stock"),
show="headings")

for c in tree4["columns"]:
    tree4.heading(c,text=c)

tree4.pack(fill="both",expand=True)

root.mainloop()