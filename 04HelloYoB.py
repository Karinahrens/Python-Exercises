#Demonstrates casting data types
#Remember "input()" returns a string value
name = input("What is your name? ")
age = input("What is your age? ")
numerical_age = int(age)
year = 2019
year_of_birth = year - numerical_age
print("Hello" , age , "years old" , name)
print("You were born in" , str(year_of_birth))

