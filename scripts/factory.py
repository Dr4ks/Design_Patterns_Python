from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "Dog":
            return Dog()
        elif animal_type == "Cat":
            return Cat()
        else:
            raise Exception(f"Invalid animal type: {animal_type}")

animal_factory = AnimalFactory()

dog = animal_factory.create_animal("Dog")
print(dog.speak()) 

cat = animal_factory.create_animal("Cat")
print(cat.speak()) 