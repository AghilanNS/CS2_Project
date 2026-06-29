#Onur
#Defining class Order
class Order:
    def __init__(self,order_num,order_type):
        self.order_num = order_num
        self.order_type = order_type
        self.items = []

    def add_item(self,item):
        self.items.append(item)

    def calculate_total(self):
        total = 0

        for item in self.items:
            total += item.price

        return total

    def display_info(self):
        item_names = []

        for item in self.items:
            item_names.append(item.name)

        return (
            f"Order Number: {self.order_num}\n"
            f"Order Type: {self.order_type}\n"
            f"Items: {', '.join(item_names)}\n"
            f"Total Price: €{self.calculate_total():.2f}"
        )