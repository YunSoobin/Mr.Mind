from abc import ABCMeta, abstractmethod

# Product
class Bread(metaclass=ABCMeta):
    @abstractmethod
    def getRecipe(self):
        pass


# Creator
class Factory(metaclass=ABCMeta):
    @abstractmethod
    def getBread(self, breadType):
        pass


# concreteProduct
class CreamBread(Bread):
    def __init__(self):
        self.breadType = "cream"
        self.flour = 100
        self.water = 100
        self.cream = 200

    def getRecipe(self):
        print("breadType :", self.breadType)
        print("recipe")
        print("flour :", self.flour)
        print("water :", self.water)
        print("cream :", self.cream)

class SugarBread(Bread):
    def __init__(self):
        self.breadType = "sugar"
        self.flour = 100
        self.water = 50
        self.sugar = 200

    def getRecipe(self):
        print("breadType :", self.breadType)
        print("recipe")
        print("flour :", self.flour)
        print("water :", self.water)
        print("sugar :", self.sugar)

class ButterBread(Bread):
    def __init__(self):
        self.breadType = "butter"
        self.flour = 100
        self.water = 100
        self.butter = 50

    def getRecipe(self):
        print("breadType :", self.breadType)
        print("recipe")
        print("flour :", self.flour)
        print("water :", self.water)
        print("butter :", self.butter)

# ConcreteCreator
class BreadFactory(Factory):
    def getBread(self):
        if self == "cream":
            recipe = CreamBread().getRecipe()
        elif self == "sugar":
            recipe = SugarBread().getRecipe()
        elif self == "butter":
            recipe = ButterBread().getRecipe()

        return recipe


breadTypes = ["cream", "sugar", "butter"]
for i in breadTypes:
    BreadFactory.getBread(i)
    print('')



