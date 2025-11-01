
import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600
apple = Actor("apple")

def draw():
    screen.clear()
    apple.pos = (randint(10, 800), randint(10, 600))  # Set random position for the apple
    apple.draw()

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("no.......apple!")
    else:
        print("the apple got his revenge mwaha ha ha ha!")
        quit() # leaves screen open; no difference

pgzrun.go()