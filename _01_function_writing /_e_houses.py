"""
Have the turtle draw a row of houses.
"""
from tkinter import messagebox, simpledialog, Tk
import turtle

if __name__ == '__main__':
    # TODO)
    #   1) Move the turtle to the left side of the window near the bottom.
    #   2) Draw ONE flat-topped house with height=100 and green grass after it.
    #   3) Put the code that drew the house into a function called draw_house
    #      HINT: Only the code that draws one house should go in this function.
    #   4) Using the function you just created, draw 10 houses.
    #      HINT: Use a for loop.
    #   5) Run the code to make sure it works before proceeding.
    #   6) Now change the draw_house function to take height as a parameter.
    #   7) Use random numbers to draw 9 houses of different heights.
    #   8) Run the code to make sure it works before proceeding.
    #   9) Make the draw_house function's height input a string and set the
    #      height of the house based on the following:
    #         “small”            =  60
    #         “medium”           =  120
    #         “large”            =  250
    #   10) Make two new functions that draw different shaped roofs
    #      (JUST the roof part): draw_pointy_roof, draw_flat_roof
    #   11) By calling the correct "roof" function, make large houses have
    #      flat roofs and all the others have pointy roofs.
    window = turtle.Screen()
    window.bgcolor('white')
    turtle = turtle.Turtle()
    turtle.shape("turtle")
    turtle.color('green')
    turtle.pencolor('red')

    for i in range (9):
        turtle.penup()
        turtle.forward(100)
        turtle.pendown()
        q1 = simpledialog.askinteger(title='home', prompt="what size house do you want?")
        turtle.speed(q1)

        for i in range(4):
            turtle.forward(q1)
            turtle.left(90)

        if q1 < 249:
            turtle.penup()
            turtle.forward(q1)
            turtle.left(90)
            turtle.forward(q1)
            turtle.left(450)
            turtle.pendown()
            turtle.forward(q1)

            for i in range(3):
                turtle.right(120)
                turtle.forward(q1)

            turtle.left(180)




