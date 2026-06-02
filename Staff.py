#Defining class Staff
class Staff:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def display_info(self):
        return f"Staff Name: {self.name}\nJob: {self.job}"
            