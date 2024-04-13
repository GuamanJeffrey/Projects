#Name: Jeffrey Guaman
#Email: JEFFREY.GUAMAN18@myhunter.cuny.edu
#Date: September 27th, 2023
#This program asks the user for a string and that string gets split up into a list of its characters and each character is used to determine the action the user wants the turtle to make. 
import turtle
t = turtle.Turtle()
x = input("Enter a string: ")
y = list(x)

for i in y:
    if (i == 'F'):
        t.forward(50)
    elif (i=='L'):
        t.left(90)
    elif (i=='R'):
        t.right(90)
    elif (i == '^'):
        t.penup()
    elif (i == 'v'):
        t.pendown()
    elif (i == 'B'):
        t.backward(50)
    elif (i == 'S'):
        t.stamp()
    elif (i == 'l'):
        t.left(45)
    elif (i == 'r'):
        t.right(45)
    elif (i == 'p'):
        t.color('purple')
        
