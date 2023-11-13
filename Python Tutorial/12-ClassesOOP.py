class Person:
    #method, initializer
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

kerim = Person("Kerim",29,"Male")


# Example

class Dog():

    year = 7

    def __init__(self,age):
        self.age = age
        self.dogHumanAge = age * self.year
        print("dog instance")

    def humanAge(self):
        return self.age * Dog.year #Dog.year -> self.year

myDog = Dog(3)

print(myDog.age)
print(myDog.humanAge())
print(myDog.dogHumanAge)

# inheritance

class Musician():

    def __init__(self,name):
        self.name = name
        print("musician class")

    def test1(self):
        print("test1")

    def test2(self):
        print("test2")

kerim = Musician("Kerim")

print(kerim.name)

class MusicianPlus(Musician):

    def __init__(self,name):
        Musician.__init__(self,name)
        print("musician plus")

    def test3(self):
        print("test3")

    #override
    def test1(self):
        print("test1 test1 test1")

guitar = MusicianPlus("Guitar")

kerim.test1()
guitar.test1()

# polymorphism

class Banana():

    def __init__(self,name):
        self.name = name

    def info(self):
        return f"150 calories {self.name}"

class Apple():

    def __init__(self,name):
        self.name = name

    def info(self):
        return f"100 calories {self.name}"

banana = Banana("banana")
apple = Apple("apple")

print(banana.info())
print(apple.info())

fruitList = [banana, apple]

for fruit in fruitList:
    print(fruit.info())

# encapsulation

class Phone():
    def __init__(self,name,price):
        self.name = name
        self.__price = price

    def info(self):
        print(f"{self.name} price is: {self.__price}")

    def changePrice(self,price):
        self.__price = price

iphone = Phone("Iphone 14",500)

iphone.info()

iphone.__price = 400
iphone.info()

iphone.changePrice(300)
iphone.info()

# abstraction

from abc import ABC, abstractmethod

class Car(ABC):

    @abstractmethod
    def maxSpeed(self):
        pass

class Tesla(Car):

    def maxSpeed(self):
        print("200km")

tesla = Tesla()

tesla.maxSpeed()

# special methods

class Fruit():

    def __init__(self,name,calories):
        self.name = name
        self.calories = calories

    def __str__(self):
        return f"{self.name}: {self.calories} calories"

    def __len__(self):
        return self.calories

fruit = Fruit("banana", 150)

print(fruit)       #__str__
print(len(fruit))  #__len__