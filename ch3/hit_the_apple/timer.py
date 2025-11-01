import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600
score = 0
apple = Actor("apple")

def draw():
    screen.clear()
    apple.pos = (randint(10, 800), randint(10, 600))  # Set random position for the apple
    apple.draw()
    screen.draw.text(f"score: {score}", topright=(WIDTH-15, 10), fontsize=40, color="sky blue")

def on_mouse_down(pos):
    global score
    if apple.collidepoint(pos):
        print("no.......apple!")
        score += 1
    else:
        print("the apple got his revenge mwaha ha ha ha!")
        quit() # leaves screen open; no difference

pgzrun.go()
