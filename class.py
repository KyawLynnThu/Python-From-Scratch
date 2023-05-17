# name="kyaw linn thu"

# print(type(name))

class Car :
    def __init__(self, name, wheels) :
        self.name=name
        self.wheels=wheels

    def drive(self) :
        print(f'{self.name} is driving')

lambo=Car("Lamborghnini", 4)
# print(lambo.name)
lambo.drive()

mercedes=Car("Mercedes", 4)
mercedes.drive()