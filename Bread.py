from abc import ABCMeta, abstractmethod

# Product
class Bread(metaclass=ABCMeta):
    @abstractmethod
    def getRecipe(self):
        pass

# concreteProduct
class Cream(Bread):
    def __init__(self, flour, water, butter):
        self.flour = flour
        self.water = water
        self.butter = butter

    def getRecipe(self):
        print("breadType : cream")
        print("recipe")
        print("flour : ", self.flour)
        print("water :", self.water)
        print("butter : ", self.butter, "\n")

class Sugar(Bread):
    def __init__(self, flour, water, butter):
        self.flour = flour
        self.water = water
        self.butter = butter

    def getRecipe(self):
        print("breadType : sugar")
        print("recipe")
        print("flour : ", self.flour)
        print("water :", self.water)
        print("butter : ", self.butter, "\n")

class Butter(Bread):
    def __init__(self, flour, water, butter):
        self.flour = flour
        self.water = water
        self.butter = butter

    def getRecipe(self):
        print("breadType : butter")
        print("recipe")
        print("flour : ", self.flour)
        print("water :", self.water)
        print("butter : ", self.butter, "\n")

# Factory
class BreadFactory:
    def getCreamBread(self):
        return Cream(100, 100, 200)

    def getSugarBread(self):
        return Sugar(100, 50, 200)

    def getButterBread(self):
        return Butter(100, 100, 50)

# client
def bread_client():
    BreadFactory().getCreamBread().getRecipe()
    BreadFactory().getSugarBread().getRecipe()
    BreadFactory().getButterBread().getRecipe()

if __name__ == '__main__':
    client = bread_client()
