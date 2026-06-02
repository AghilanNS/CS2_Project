#Defining class Table
class Table:
    def __init__(self, table_num, num_of_customers):
        self.table_num = table_num
        self.num_of_customers = num_of_customers
        self.total_bill = 0.0
        self.payment_status = "Unpaid"

    def add_to_bill(self, amount):
        self.total_bill += amount

    def make_payment(self):
        self.payment_status = "Paid"

    def display_info(self):
        return (
            f"Table Number: {self.table_num}\n"
            f"Number of Customers: {self.num_of_customers}\n"
            f"Total Bill: €{self.total_bill:.2f}\n"
            f"Payment Status: {self.payment_status}")