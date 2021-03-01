# Exercise 4
# Refactor the Pet class from the previous example so that it has a class variable
# allowed_species that contains a list of all the species that can be added to the class. During
# initialisation check that the species that is being created is an allowed species

class Pet:
    allowed_species = ('Dog', 'Cat')

    def __init__(self, name, species):
        self.name = name
        self.species = species
        if species in self.allowed_species:
            print("This is a pet:")
        else:
            print("This is not a Pet:")

    def namespecie(self):
        return '{} is a {}'.format(self.name, self.species)

# example
pet_8 = Pet('Branco', 'Horse')
print(pet_8.namespecie())
