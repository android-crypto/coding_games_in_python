
import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600

kid = Actor("kid")

def draw():
    screen.clear()
    kid.pos = (randint(10, 800), randint(10, 600))  # Set random position for the apple
    kid.draw()

def on_mouse_down(pos):
    if kid.collidepoint(pos):
        print("Good shot! You hit the kid!")
    else:
        print("Game over!")
        quit() # leaves screen open; no difference

pgzrun.go()
