
import pgzrun
from random import randint

WIDTH = 800
HEIGHT=600
orange = Actor("orange")

def draw():
    screen.clear()
    orange.pos = (randint(10, 600), randint(10, 600))  # Set random position for the orange
    orange.draw()

def on_mouse_down(pos):
    if orange.collidepoint(pos):
        print("no........................................................................................oooooooorrrrrrrrrraaaaaaaaaaaaannnnnnnnnnnnggggggggggggggeeeeee!!!")
    else:
        print("the orange got his revenge mwaha ha ha ha!")
        quit() # leaves screen open; no difference

pgzrun.go()