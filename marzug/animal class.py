
class Animals:
    def __init__(self, name, home,):
        self.name = name
        self.home = home
    def display(self):
        print("name:", self.name)
        print("home:", self.home)
    def call(self, number):
        print("Calling", number)
dog = Animals("dog", "kennal")
cow = Animals("cow", "kraal")
dog.display()
cow.display()