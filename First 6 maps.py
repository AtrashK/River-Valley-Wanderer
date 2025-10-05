import turtle
from turtle import Shape, Turtle
from tkinter import PhotoImage
import tkinter
import time
import math
 
# making the turtle screen
screen=turtle.getscreen()
screenTk = screen.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", 1)
turtle.ht()

# getting the coordinates of the cursor
canvas = turtle.getcanvas()
x, y = canvas.winfo_pointerx(), canvas.winfo_pointery()

Above_spawn = PhotoImage(file="./Maps/Above-spawn-map.gif").zoom(6, 6)
screen.addshape("Above_spawn", Shape("image", Above_spawn))

Below_spawn = PhotoImage(file="./Maps/Below-spawn-map.gif").zoom(6, 6)
screen.addshape("Below_spawn", Shape("image", Below_spawn))

Left_of_spawn = PhotoImage(file="./Maps/Left-of-spawn-map.gif").zoom(6, 6)
screen.addshape("Left_of_spawn", Shape("image", Left_of_spawn))

Spawn = PhotoImage(file="./Maps/Spawn-map.gif").zoom(6, 6)
screen.addshape("Spawn", Shape("image", Spawn))

Top_left_from_spawn = PhotoImage(file="./Maps/Top-left-from-spawn-map.gif").zoom(6, 6)
screen.addshape("Top_left_from_spawn", Shape("image", Top_left_from_spawn))

Top_right_from_spawn = PhotoImage(file="./Maps/Top-right-from-spawn-map.gif").zoom(6, 6)
screen.addshape("Top_right_from_spawn", Shape("image", Top_right_from_spawn))

Above_spawn=Turtle("Above_spawn")
Above_spawn.ht()

Below_spawn=Turtle("Below_spawn")
Below_spawn.ht()

Left_of_spawn=Turtle("Left_of_spawn")
Left_of_spawn.ht()

Spawn=Turtle("Spawn")
Spawn.ht()

Top_left_from_spawn=Turtle("Top_left_from_spawn")
Top_left_from_spawn.ht()

Top_right_from_spawn=Turtle("Top_right_from_spawn")
Top_right_from_spawn.ht()

def two():
    Above_spawn.st()
    Below_spawn.ht()
    Left_of_spawn.ht()
    Spawn.ht()
    Top_left_from_spawn.ht()
    Top_right_from_spawn.ht()

def six():
    Above_spawn.ht()
    Below_spawn.st()
    Left_of_spawn.ht()
    Spawn.ht()
    Top_left_from_spawn.ht()
    Top_right_from_spawn.ht()

def four():
    Above_spawn.ht()
    Below_spawn.ht()
    Left_of_spawn.st()
    Spawn.ht()
    Top_left_from_spawn.ht()
    Top_right_from_spawn.ht()

def five():
    Above_spawn.ht()
    Below_spawn.ht()
    Left_of_spawn.ht()
    Spawn.st()
    Top_left_from_spawn.ht()
    Top_right_from_spawn.ht()

def one():
    Above_spawn.ht()
    Below_spawn.ht()
    Left_of_spawn.ht()
    Spawn.ht()
    Top_left_from_spawn.st()
    Top_right_from_spawn.ht()

def three():
    Above_spawn.ht()
    Below_spawn.ht()
    Left_of_spawn.ht()
    Spawn.ht()
    Top_left_from_spawn.ht()
    Top_right_from_spawn.st()


def game():

    screen.listen()
    screen.onkeypress(one, "1")
    screen.onkeypress(two, "2")
    screen.onkeypress(three, "3")
    screen.onkeypress(four, "4")
    screen.onkeypress(five, "5")
    screen.onkeypress(six, "6")
    

    screen.ontimer(game, 20)

game()

screen.mainloop()