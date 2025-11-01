
import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600

roland = Actor("roland")

def draw():
    screen.clear()
    roland.pos = (randint(10, 800), randint(10, 600))  # Set random position for the apple
    roland.draw()

def on_mouse_down(pos):
    if roland.collidepoint(pos):
        print("Good shot! You hit roland!")
    else:
        print("Game over!")
        quit() # leaves screen open; no difference

pgzrun.go()
