#Onur
#Combined Menu Item Class(after feedback)
#Contains previous classes; Food, Beverage, Snacks
#Defining class MenuItem
class MenuItem:
    def __init__(self,item_id,name,category,price):
        
        self.item_id = item_id
        self.name = name
        self.category = category #Food,Beverage, Snack
        self.price = price

    def display_info(self):
        return (
            f"ID: {self.item_id}\n"
            f"Name: {self.name}\n"
            f"Category: {self.category}\n"
            f"Price: €{self.price:.2f}\n"
        )
