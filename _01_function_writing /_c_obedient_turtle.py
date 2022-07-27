"""
Make an obedient turtle that will obey commands to draw shapes.
"""
from tkinter import messagebox, simpledialog, Tk
import turtle


if __name__ == '__main__':
    # TODO)
    #   1. Create a turtle.
    #   2. Write 3 method definitions for drawing a square, triangle, and
    #      circle.
    #   3. Ask the user for the for a shape to draw.
    #   4. Draw the appropriate shape depending on their answer (call the right
    #      function)
    if __name__ == '__main__':
        window = turtle.Screen()
        window.bgcolor('white')
        turtle = turtle.Turtle()
        turtle.shape("turtle")
        turtle.speed(0)
        turtle.color('green')
        turtle.pencolor('red')

    q1 = simpledialog.askstring(title='1?', prompt="what shape do you want, triangle circle hexegon or square?")

    turtle.width(100)

    if q1 == "circle":
        messagebox.showinfo(message='look, a car on the rood')
        for i in range(100):
            turtle.pencolor('black')
            turtle.forward(10)
            turtle.left(9)


    if q1 == "triangle":
        for i in range(30):
            turtle.forward(100)
            turtle.left(120)

    if q1 == "square":
        for i in range(16):
            turtle.forward(100)
            turtle.left(90)

    if q1 == "hexegon":
        for i in range(30):
            turtle.forward(100)
            turtle.left(72)
