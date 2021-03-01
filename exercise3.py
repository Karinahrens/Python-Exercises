#Write a program to find the greatest of three numbers entered by the user. Remember to
#comment your code and to use meaningful variable names.

n_1=int(input("Please insert first number "))
n_2=int(input("Please insert second number "))
n_3=int(input("Please insert third number "))

if (n_1>=n_2) and (n_1>=n_3):
    great=n_1
elif (n_2>=n_1) and (n_2>=n_3):
    great=n_2
else:
    great=n_3
print('Greatest of three numbers is :', great)