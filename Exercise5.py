#The Magic Kingdom theme park has some rides that are restricted by age and height. The owner
#of the park wants to reduce the delays and disappointment caused by park-goers not knowing
#the restrictions before queuing for the rides. He wants to install software on terminals around
#the park so that people can find out which rides they may go on and he provides the following
#information:
#Ride name Age Restrictions Height Restrictions
#1 Carnival Carousel Min 5 years old None None
#2 Dodgems Min 12 years old Min 1.3m
#3 Pandemonium Min 16 and Max 70 years old Min 1.4m and Max 2m
#4 Phantom Ghost Zone Min 8 years old None
#5 Scenic River Cruise None None
#Write a program that displays available ride names and code numbers as shown in the table
#above and asks users to enter the code number of the ride they’ve selected. The program
#should then ask for their age and height, and accordingly display a message indicating whether
#or not they can go on their chosen ride. The park owner is happy with text input for now.
#Remember to comment your code and to use meaningful variable names.

print("Welcome to Magic Kingdom! ")
print("For Carnival Carousel press=[1]")
print("Dodgems press=[2]")
print("Pandemonium press=[3]")
print("Phantom Ghost Zone=[4]")
print("Scenic River Cruise=[5]")
ride=int(input("Please select which ride you want to go and discover if you can: "))
if not(1 <= ride <= 5):
    print("You've entered a ride number that does not exist! Please try again.")
age=int(input("What's your age? "))
height=float(input("What's your height(in meters)? "))

if ride==1:
    if age>=5:
    print("You can GO!")
else :
    print("Sorry, min 5 years old")
if ride==2:
    if age>=12 and height>=1.3:
    print("YOU can GO")
else :
    print("Sorry, min 12 years old and 1.2 height")
if ride==3 :
    if age>16 and age<70 and height>1.4 and height<2:
    print("YOU can GO")
else:
    print("Sorry You Can't go")
if ride==4:
    print("YOU Can GO!!")
