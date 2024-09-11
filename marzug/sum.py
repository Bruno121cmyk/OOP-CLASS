class items:
    def __init__(self, name, cost,profit):
        self.name = name
        self.cost = cost
        self.profit= profit
    def display(self):
        print("name:", self.name)
        print("cost:", self.cost)
        print("profit:",self.profit)
    def call(self, number):
        print("Calling", number)
HP = items("elitebook840G6", "1.2M","200K")
Dell= items("latitude e7400", "1m","300k")
HP.display()
Dell.display()