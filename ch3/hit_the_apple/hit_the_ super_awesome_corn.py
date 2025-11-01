
import pgzrun
from random import randint

WIDTH = 800
HEIGHT=600
super_awesome_corn = Actor("super_awesome_corn")

def draw():
    screen.clear()
    super_awesome_corn.pos = (randint(10, 600), randint(10, 600))  # Set random position for the orange
    orange.draw()

def on_mouse_down(pos):
    if super_awesome_corn.collidepoint(pos):
        print("no............................................................................................................................................................................................super_awesome_corn super_awesome_corn!!!")
    else:
        print("the super_awesome_corn got his revenge mwaha ha ha ha!")
        quit() # leaves screen open; no difference

pgzrun.go()