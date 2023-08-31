class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Dis what? ", self.name)

person1 = Person("Deez Nuts")
person1.say_hi()
