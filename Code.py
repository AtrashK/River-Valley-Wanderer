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


screen.mainloop()