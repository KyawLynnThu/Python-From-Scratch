# name="kyaw linn thu"

# print(type(name))

class Car :
    steeringWheel=1 #class level attribute || for same method in every methods
    def __init__(self, name, wheels) :
        self.name=name #instance level attribute
        self.wheels=wheels

    def drive(self) :
        print(f'{self.name} is driving')

    @classmethod
    def common(cls) :
        print(f'All car have only {cls.steeringWheel}')

# lambo=Car("Lamborghnini", 4)
# # print(lambo.name)
# lambo.drive()

# print(lambo.steeringWheel) #class level attribute, method can use from object
# print(lambo.common())

# mercedes=Car("Mercedes", 4)
# mercedes.drive()

# instance level method
# ---------------------
#  Create object first. Run method from object

# print(Car.steeringWheel)
# Car.common()

