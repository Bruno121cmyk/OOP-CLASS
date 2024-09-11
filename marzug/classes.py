# Define the phone class
class Phone:
    # Constructor to initialize the phone object
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    # Method to display the details
    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)
    
    # Method to call the phone
    def call(self, number):
        print("Calling", number)

# Create an object of the Phone class
samsung = Phone("Samsung", "S10+", 550000)
tecno = Phone("Tecno", "Spark8", 450000)

# Call the display method
samsung.display()
tecno.display()