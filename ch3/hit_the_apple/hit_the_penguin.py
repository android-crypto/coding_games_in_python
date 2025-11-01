
import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600
penguin = Actor("penguin")

def draw():
    screen.clear()
    penguin.pos = (randint(10, 800), randint(10, 600))  # Set random position for the penguin
    penguin.draw()

def on_mouse_down(pos):
    if penguin.collidepoint(pos):
        print("penguin!")
    else:
        print("lose penguin!")
        quit() # leaves screen open; no difference

pgzrun.go()