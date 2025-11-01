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
    
roland = Actor("roland")

def draw():
    screen.clear()
    roland.pos = (randint(10, 800), randint(10, 600))  # Set random position for the apple
    roland.draw()

def on_mouse_down(pos):
    if roland.collidepoint(pos):
        print("Good shot! You hit roland!")  

orange = Actor("orange")

def draw():
    screen.clear()
    orange.pos = (randint(10, 600), randint(10, 600))  # Set random position for the orange
    orange.draw()

def on_mouse_down(pos):
    if orange.collidepoint(pos):
        print("no........................................................................................oooooooorrrrrrrrrraaaaaaaaaaaaannnnnnnnnnnnggggggggggggggeeeeee!!!")

superawesomecorn = Actor("superawesomecorn")

def draw():
    screen.clear()
    superawesomecorn.pos = (randint(10, 800), randint(10, 600))  # Set random position for the superawesomecorn
    superawesomecorn.draw()

def on_mouse_down(pos):
    if superawesomecorn.collidepoint(pos):
        print("Good shot! You hit superawesomecorn!") 

penguin = Actor("penguin")

def draw():
    screen.clear()
    penguin.pos = (randint(10, 800), randint(10, 600))  # Set random position for the penguin
    penguin.draw()

def on_mouse_down(pos):
    if penguin.collidepoint(pos):
        print("penguin!")

pgzrun.go()    