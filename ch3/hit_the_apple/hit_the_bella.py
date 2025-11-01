
import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600
bella = Actor("bella")

def draw():
    screen.clear()
    bella.pos = (randint(10, 800), randint(10, 600))  # Set random position for the bella
    bella.draw()

def on_mouse_down(pos):
    if bella.collidepoint(pos):
        print("bella!")
    else:
        print("lose bella!")
        quit() # leaves screen open; no difference

pgzrun.go()