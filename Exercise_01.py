# Exercise 1
# Implement an example for Polymorphism. Assume you have an abstract class Vehicle that provides
# the structure for the methods accelerate() and brake(). Declare two child classes Motorcycle and Bus
# that inherit from Vehicle. Implement the methods and write some test code. The methods should
# return a string that indicates in which class the method has been called.

class Vehicle:
    def __init__(self, accelerate, brake):
        self.accelerate = accelerate
        self.brake = brake

    def acceleration(self):
        print(self.accelerate)

    def brake(self):
        print(self.brake)


class Motorcycle(Vehicle):
    def __init__(self, accelerate):
        super()


class Bus(Vehicle):
    def _