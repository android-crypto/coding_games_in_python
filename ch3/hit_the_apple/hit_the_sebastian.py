
import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600

sebastian = Actor("sebastian")

def draw():
    screen.clear()
    sebastian.pos = (randint(10, 800), randint(10, 600))  # Set random position for the sebastian
    sebastian.draw()

def on_mouse_down(pos):
    if sebastian.collidepoint(pos):
        print("sebastian!")
    else:
        print("lose sebastian!")
        quit() # leaves screen open; no difference

pgzrun.go()