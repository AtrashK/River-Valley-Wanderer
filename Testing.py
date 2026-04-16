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

Down1 = PhotoImage(file="./Player/Down1.gif").zoom(6, 6)
screen.addshape("Down1", Shape("image", Down1))
Down2 = PhotoImage(file="./Player/Down2.gif").zoom(6, 6)
screen.addshape("Down2", Shape("image", Down2))
Down3 = PhotoImage(file="./Player/Down3.gif").zoom(6, 6)
screen.addshape("Down3", Shape("image", Down3))
Down4 = PhotoImage(file="./Player/Down4.gif").zoom(6, 6)
screen.addshape("Down4", Shape("image", Down4))
Down5 = PhotoImage(file="./Player/Down5.gif").zoom(6, 6)
screen.addshape("Down5", Shape("image", Down5))
Down6 = PhotoImage(file="./Player/Down6.gif").zoom(6, 6)
screen.addshape("Down6", Shape("image", Down6))

player=Turtle("Down1")
player.up()
player.goto(0,300)
time.sleep(2)

for i in range(1000):
    if (i%6==0):
        player.shape("Down1")
    elif (i%6==1):
        player.shape("Down2")
    elif (i%6==2):
        player.shape("Down3")
    elif (i%6==3):
        player.shape("Down4")
    elif (i%6==4):
        player.shape("Down5")
    else:
        player.shape("Down6")
    player.sety(player.ycor()-(5))
    time.sleep(0.2)

screen.update()
screen.mainloop()