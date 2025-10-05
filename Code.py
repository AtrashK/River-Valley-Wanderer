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

key_held_w=False
key_held_s=False
key_held_a=False
key_held_d=False

screen.tracer(0)

# getting the coordinates of the cursor
canvas = turtle.getcanvas()
x, y = canvas.winfo_pointerx(), canvas.winfo_pointery()

player=turtle.Turtle()
player.up()
player.shape("circle")
player.shapesize(3,3,1)

stuff=turtle.Turtle()
stuff.ht()

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
Spawn.st()

Top_left_from_spawn=Turtle("Top_left_from_spawn")
Top_left_from_spawn.ht()

Top_right_from_spawn=Turtle("Top_right_from_spawn")
Top_right_from_spawn.ht()

map=5

def press_w():
    global key_held_w
    key_held_w = True
def release_w():
    global key_held_w
    key_held_w = False

def press_s():
    global key_held_s
    key_held_s = True
def release_s():
    global key_held_s
    key_held_s = False

def press_a():
    global key_held_a
    key_held_a = True
def release_a():
    global key_held_a
    key_held_a = False

def press_d():
    global key_held_d
    key_held_d = True
def release_d():
    global key_held_d
    key_held_d = False

def player_movement():
    global key_held_w, key_held_s, key_held_a, key_held_d
    if key_held_w:
        player.sety(player.ycor()+10)
    if key_held_s:
        player.sety(player.ycor()-10)
    if key_held_a:
        player.setx(player.xcor()-10)
    if key_held_d:
        player.setx(player.xcor()+10)

def map_change(direction):
    global map
    if (direction=="up"):
        map+=3
        player.sety(-390)

    if (map==3):
        Spawn.ht()
        Above_spawn.st()

    return direction


def game():
    stuff.clear()
    screen.listen()
    screen.onkeypress(press_w, "w")
    screen.onkeyrelease(release_w, "w")
    screen.onkeypress(press_s, "s")
    screen.onkeyrelease(release_s, "s")
    screen.onkeypress(press_a, "a")
    screen.onkeyrelease(release_a, "a")
    screen.onkeypress(press_d, "d")
    screen.onkeyrelease(release_d, "d")

    player_movement()

    if (player.ycor()>460):
        map_change(up)
    if (player.ycor()<-460):
        map_change(down)
    if (player.xcor()>790):
        map_change(right)
    if (player.ycor()<-790):
        map_change(left)

    screen.update()
    screen.ontimer(game, 20)

game()

screen.update()
screen.mainloop()