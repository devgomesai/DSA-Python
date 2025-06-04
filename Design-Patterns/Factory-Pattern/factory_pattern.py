class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement me")
    
class Dog(Animal):
    def speak():
        return "Woof!"
    
class Cat(Animal):
    def speak():
        return "Meow!"
    
class AnimalFactory:
    @staticmethod
    def get_animal(animal_type:str)->Animal:
        if animal_type.lower() == 'dog':
            return Dog
        elif animal_type.lower() == 'cat':
            return Cat
        else:
            raise ValueError("Unknown Animal")
        
animal = AnimalFactory.get_animal('DOG')
print(animal.speak())