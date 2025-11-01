import pgzrun
from random import randint

score = 0
WIDTH = 800
HEIGHT = 600

apple = Actor("apple")

def draw():
    screen.clear()
    apple.pos = (randint(10, 800), randint(10, 600))  # Set random position for the apple
    apple.draw()
    screen.draw.text (f"Score: {score}", topright=(WIDTH-15, 10), fontsize=30, color="white")

def close_game():
    print("Closing game...")
    quit()

def on_mouse_down(pos):
    global score, game_over
    if apple.collidepoint(pos):
        score += 1
        print(f"Good shot! You hit the moving apple. Your score is {score}. ")
    else:
        print(f"Oops! Game over! You missed the moving apple! Your score was {score}")
        clock.schedule_unique(close_game, 2.0)

pgzrun.go() 
