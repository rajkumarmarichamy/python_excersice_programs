def walk():
    print("walk")


class Mammal:
    pass


def bark():
    print("bark")


class Dog(Mammal):
    def walk(self):
        print("walk")
        pass


class Cat(Mammal):
    pass


dog1 = Dog()
dog1.walk()
cat1 = Cat()
walk()
