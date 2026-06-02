#Defining class Delivery
class Delivery:
    def __init__(self,driver_name,delivery_address, order_num):
        self.driver_name = driver_name
        self.delivery_address = delivery_address
        self.order_num = order_num

    def display_info(self):
        return (
            f"Driver Name: {self.driver_name}\n"
            f"Delivery Address: {self.delivery_address}\n"
            f"Order Number: {self.order_num}"
            )