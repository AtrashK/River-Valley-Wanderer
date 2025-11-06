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

MAPS=[]

screen.tracer(0)

# getting the coordinates of the cursor
canvas = turtle.getcanvas()
x, y = canvas.winfo_pointerx(), canvas.winfo_pointery()

stuff=turtle.Turtle()
stuff.ht()

esf_x=math.floor(screen.window_width()/256)
esf_y=math.floor(screen.window_height()/144)

Above_spawn = PhotoImage(file="./Maps/Above-spawn-map.gif").zoom(esf_x, esf_y)
screen.addshape("Above_spawn", Shape("image", Above_spawn))

Below_spawn = PhotoImage(file="./Maps/Below-spawn-map.gif").zoom(esf_x, esf_y)
screen.addshape("Below_spawn", Shape("image", Below_spawn))

Left_of_spawn = PhotoImage(file="./Maps/Left-of-spawn-map.gif").zoom(esf_x, esf_y)
screen.addshape("Left_of_spawn", Shape("image", Left_of_spawn))

Spawn = PhotoImage(file="./Maps/Spawn-map.gif").zoom(esf_x, esf_y)
screen.addshape("Spawn", Shape("image", Spawn))

Top_left_from_spawn = PhotoImage(file="./Maps/Top-left-from-spawn-map.gif").zoom(esf_x, esf_y)
screen.addshape("Top_left_from_spawn", Shape("image", Top_left_from_spawn))

Top_right_from_spawn = PhotoImage(file="./Maps/Top-right-from-spawn-map.gif").zoom(esf_x, esf_y)
screen.addshape("Top_right_from_spawn", Shape("image", Top_right_from_spawn))

Above_spawn=Turtle("Above_spawn")
Above_spawn.ht()
MAPS.append(Above_spawn)

Below_spawn=Turtle("Below_spawn")
Below_spawn.ht()
MAPS.append(Below_spawn)

Left_of_spawn=Turtle("Left_of_spawn")
Left_of_spawn.ht()
MAPS.append(Left_of_spawn)

Spawn=Turtle("Spawn")
Spawn.st()
MAPS.append(Spawn)

Top_left_from_spawn=Turtle("Top_left_from_spawn")
Top_left_from_spawn.ht()
MAPS.append(Top_left_from_spawn)

Top_right_from_spawn=Turtle("Top_right_from_spawn")
Top_right_from_spawn.ht()
MAPS.append(Top_right_from_spawn)

Down1 = PhotoImage(file="./Player/Down1.gif").zoom(esf_x, esf_y)
screen.addshape("Down1", Shape("image", Down1))
Down2 = PhotoImage(file="./Player/Down2.gif").zoom(esf_x, esf_y)
screen.addshape("Down2", Shape("image", Down2))
Down3 = PhotoImage(file="./Player/Down3.gif").zoom(esf_x, esf_y)
screen.addshape("Down3", Shape("image", Down3))
Down4 = PhotoImage(file="./Player/Down4.gif").zoom(esf_x, esf_y)
screen.addshape("Down4", Shape("image", Down4))
Down5 = PhotoImage(file="./Player/Down5.gif").zoom(esf_x, esf_y)
screen.addshape("Down5", Shape("image", Down5))
Down6 = PhotoImage(file="./Player/Down6.gif").zoom(esf_x, esf_y)
screen.addshape("Down6", Shape("image", Down6))

player=Turtle("Down1")
player.up()

map=8

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

def boundaries():
    global map
    while map==8:
        return True

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

def hide_all_maps():
    for i in MAPS:
        i.ht()

def map_change(direction):
    global map
    if (direction=="up"):
        map-=5
        player.sety(-390)
    elif (direction=="down"):
        map+=5
        player.sety(390)
    elif (direction=="right"):
        map+=1
        player.setx(-750)
    elif (direction=="left"):
        map-=1
        player.setx(750)

    hide_all_maps()
    if (map==2):
        Top_left_from_spawn.st()
    elif (map==3):
        Above_spawn.st()
    elif (map==4):
        Top_right_from_spawn.st()
    elif (map==7):
        Left_of_spawn.st()
    elif (map==8):
        Spawn.st()
    elif (map==13):
        Below_spawn.st()

    return direction

n=1

def game():
    global map, player, n
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
        map_change("up")
    if (player.ycor()<-460):
        map_change("down")
    if (player.xcor()>790):
        map_change("right")
    if (player.xcor()<-790):
        map_change("left")
        
    screen.update()
    screen.ontimer(game, 30)

game()

screen.update()
screen.mainloop()