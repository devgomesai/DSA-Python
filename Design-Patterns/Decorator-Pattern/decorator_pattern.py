
##### Coffee Class #####
class Coffee:
    @staticmethod
    def cost():
        return 5
    
    @staticmethod
    def description():
        return "Coffee"
##### Milk Class #####
class MilkDecorator:
    def __init__(self, coffee: Coffee):
        self.coffee = coffee
        
    def cost(self):
        return self.coffee.cost() + 1
    
    def description(self):
        return self.coffee.description() + " with Milk"
##### Sugar Class #####
class SugarDecorator:
    def __init__(self, coffee: Coffee):
        self.coffee = coffee
        
    def cost(self):
        return self.coffee.cost() + 0.5
    
    def description(self):
        return self.coffee.description() + " with sugar"
########################
my_coffee = Coffee()
print("Base:", my_coffee.description(), ", Cost:", my_coffee.cost())

my_coffee = MilkDecorator(my_coffee)
print("After Milk:", my_coffee.description(), ", Cost:", my_coffee.cost())

my_coffee = SugarDecorator(my_coffee)
print("After Sugar:", my_coffee.description(), ", Cost:", my_coffee.cost())
        
    