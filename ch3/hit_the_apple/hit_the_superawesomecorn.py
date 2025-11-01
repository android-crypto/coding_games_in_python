
import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600

superawesomecorn = Actor("superawesomecorn")

def draw():
    screen.clear()
    superawesomecorn.pos = (randint(10, 800), randint(10, 600))  # Set random position for the superawesomecorn
    superawesomecorn.draw()

def on_mouse_down(pos):
    if superawesomecorn.collidepoint(pos):
        print("Good shot! You hit superawesomecorn!")
    else:
        print("Game over!")
        quit() # leaves screen open; no difference

pgzrun.go()
