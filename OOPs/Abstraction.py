from abc import ABC, abstractmethod


class Dog(ABC):                                             #SuperClass
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

    def display_name(self):
        print(f"Dog's name: {self.name}")


class Labordor(Dog):                                        #SubClass
    def sound(self):
        print("Labordor Woof!")


class Pitbull(Dog):                                         #SubClass
    def sound(self):
        print("Pitbull Bow!")


dogs = [Labordor("Charlie"), Pitbull("Rocky")]
for dog in dogs:
    dog.display_name()
    dog.sound()
