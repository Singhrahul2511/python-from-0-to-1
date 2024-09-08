class animals():
    pass

class pets(animals):
    pass

class Dog(pets):

    @staticmethod
    def bark():
        print("Bow Bow!")

d =Dog()
d.bark()