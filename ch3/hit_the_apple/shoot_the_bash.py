import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600
the = Actor("the")

def draw():
    screen.clear()
    the.pos = (randint(10, 800), randint(10, 600))  # Set random position for the the
    the.draw()

def on_mouse_down(pos):
    if the.collidepoint(pos):
        print("no!")
    else:
        print("the thing got his revenge mwaha ha ha ha!")
        quit() # leaves screen open; no difference

pgzrun.go()