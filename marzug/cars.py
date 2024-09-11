
class cars:
    def __init__(self, name, country, price):
        self.name = name
        self.country = country
        self.price =price
    def display(self):
        print("name:", self.name)
        print("country:", self.country)
        print("price:", self.price)
    def call(self, number):
        print("Calling", number)
Mercedesbenz =cars("Mercedes-benz", "Germany","200m")
Rangerover = cars("Range-rover", "England","300m")
Mercedesbenz.display()
Rangerover.display()