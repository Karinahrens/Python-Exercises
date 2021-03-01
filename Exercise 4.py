# It is not always possible to form a triangle given any three lines! For example, if one of the lines is
# 9cm long, one of the others is 3cm long and the third is 2cm long, you will not be able to get the
# edges of all three lines to meet and you cannot therefore form a triangle.
# There is a simple test using the Triangle Inequality Theorem to check if it is possible to form a
# triangle given three line lengths:
#  If the sum of any two lengths is always greater than the third, then a triangle can be formed
# using those lengths. Otherwise, it cannot.
#  If the sum of any two lengths equals the third, then a "degenerate" triangle is formed instead.
# Write Python code to prompt the user to input three line lengths, and then determine whether
# they can form a triangle. Display the result to the user on the PyCharm console. Remember to
# comment your code and to use meaningful variable names.
#

print("Let's check if a triangle can be formed...")
x = int(input("Enter first lenght of triangle: "))
y = int(input("Enter second triangle`s lenght: "))
z = int(input("Enter third triangle`s lenght: "))

if x + y > z and z + y > x and x + z > y:
    print('Good! Triangle can be formed!')
elif x + y == z or x + z == y or z + y == x:
    print("The triangle is degenerate.")
else:
    print("Triangle can't be formed, try again")
