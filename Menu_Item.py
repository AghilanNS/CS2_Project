#Combined Menu Item Class(after feedback)
#Contains previous classes; Food, Beverage, Snacks, Meal Set

class MenuItem:
    def __init__(self,item_id,name,category,price,temperature="N/A",with_ice="N/A",cooked_level="N/A"):
        
        self.item_id = item_id
        self.name = name
        self.category = category #Food,Beverage, Snack
        self.price = price
        self.temperature = temperature #for drinks (hot/cold)
        self.with_ice = with_ice
        self.cooked_level = cooked_level

    def display_info(self):
        return (
            f"ID: {self.item_id}\n"
            f"Name: {self.name}\n"
            f"Category: {self.category}\n"
            f"Price: €{self.price:.2f}\n"
            f"Temperature: {self.temperature}\n"
            f"With Ice: {self.with_ice}\n"
            f"Cooked Level: {self.cooked_level}"
        )
