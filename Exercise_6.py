# Exercise 6
# Implement the task from 5 in a more Pythonic way using a property decorator. Test the code
# using examples.
# A getter is a method that gets the value of a property. this helps to access private attributes from a class.
# A setter is a method that sets the value of a property. this helps to set the value to private attributes in a class.

class Pet:
    allowed_species = ('Dog', 'Cat')

    def __init__(self, species):
        self._species = species

    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, species):
        if species in self.allowed_species:
            print("Allowed")
        else:
            print("Not a pet")


pet_1 = Pet('Dog')

pet_1.species ='Dog'

print(pet_1.species)
