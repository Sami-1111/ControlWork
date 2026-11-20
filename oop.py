
from abc import ABC, abstractmethod


# 1. Инкапсуляция
class Person:
    def __init__(self):
        self._age = 0

    def set_age(self, age):
        if age < 0:
            print("Возраст не может быть отрицательным!")
        else:
            self._age = age

    def get_age(self):
        return self._age


person = Person()
person.set_age(20)
print("Возраст:", person.get_age())


# 2. Наследование
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"


class Dog(Animal):
    def speak(self):
        return "Гав-гав"


class Cat(Animal):
    def speak(self):
        return "Мяу"


class Bird(Animal):
    def speak(self):
        return "Чик-чирик"


dog = Dog("Рекс")
cat = Cat("Мурка")
bird = Bird("Кеша")

print(dog.name, dog.speak())
print(cat.name, cat.speak())
print(bird.name, bird.speak())


# 3. Полиморфизм
class Vehicle:
    def move(self):
        return "Транспорт движется"


class Car(Vehicle):
    def move(self):
        return "Машина едет по дороге"


class Bicycle(Vehicle):
    def move(self):
        return "Велосипед крутит педали"


class Airplane(Vehicle):
    def move(self):
        return "Самолёт летит в небе"


def move(vehicle):
    return vehicle.move()


car = Car()
bike = Bicycle()
airplane = Airplane()

print(move(car))
print(move(bike))
print(move(airplane))


# 4. Абстракция
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


rectangle = Rectangle(8, 7)
circle = Circle(5)

print("Площадь прямоугольника:", rectangle.area())
print("Площадь круга:", circle.area())
