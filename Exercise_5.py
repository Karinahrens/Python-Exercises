# Exercise 5
# Write a getter and setter method for the variable species. The setter method needs to check
# that species is an allowed species. Test the code using examples.

# A getter is a method that gets the value of a property. this helps to access private attributes from a class.
# A setter is a method that sets the value of a property. this helps to set the value to private attributes in a class.

class Pet:
    allowed_species = ('Dog', 'Cat')

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getspecies(self):
        return self.species

    def setspecies(self, species):
        if species in self.allowed_species:
            print("Allowed")
        else:
            print("Not a pet")


pet_1 = Pet("Sofia", "Cat")

pet_1.setspecies("Cat")

print(pet_1.getspecies())
