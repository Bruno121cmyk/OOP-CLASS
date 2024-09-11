
class countries:
    def __init__(self, continent, population,):
        self.continent = continent
        self.population = population
    def display(self):
        print("continent:", self.continent)
        print("population:", self.population)
    def call(self, number):
        print("Calling", number)
uganda = countries("Africa", "48millions")
kenya= countries("Africa", "55millions")
uganda.display()
kenya.display()