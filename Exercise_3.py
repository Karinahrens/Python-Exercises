# Exercise 3
# Define a class called Pet that takes a name and species at initialisation. The class has two
# methods that return the name and species respectively. Test your code with examples.

#creating class and function with name and specie
class Pet:
    def __init__(self, name, specie):
        self.name = name
        self.specie = specie

    def namespecie(self):
        return '{} {}'.format(self.name, self.specie)

# examples
pet_1 = Pet('Dexter', 'Cat')
pet_2 = Pet('Tuca', 'Dog')
pet_3 = Pet('Odim', 'Dog')
pet_4 = Pet('Hooguie', 'Cat')
pet_5 = Pet('Lilica', 'Dog')
pet_6 = Pet('Sofia', 'Cat')
pet_7 = Pet('Pantera', 'Dog')

print(pet_1.namespecie())
print(pet_2.namespecie())
print(pet_3.namespecie())
print(pet_4.namespecie())
print(pet_5.namespecie())
print(pet_6.namespecie())
print(pet_7.namespecie())
