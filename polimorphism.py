class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Error text")


class Dog(Animal):
    def speak(self):
        return self.name + ' says woof!'

class Cat(Animal):
    def speak(self):
        return self.name + ' says meow!'

dog = Dog('Dog')
chaki = Cat('Chaki')
print(dog.speak())
print(chaki.speak())