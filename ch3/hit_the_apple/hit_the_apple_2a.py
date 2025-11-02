import pgzrun
from random import randint

score, remaining_time = 0, 90
game_over = False
WIDTH = 800
HEIGHT = 600

apple = Actor("apple")

def draw():
    screen.clear()
    apple.pos = (randint(10, 800), randint(10, 600))  # Set random position for the apple
    apple.draw()
    screen.draw.text (f"Score: {score}", topright=(WIDTH-15, 10), fontsize=30, color="white")
    screen.draw.text(f"Time: {remaining_time}s", topleft=(10, 10), fontsize=30)
    
def update_timer():
    global remaining_time, game_over
    if not game_over:    
        remaining_time -= 1
        if remaining_time <= 0:
            game_over = True
            clock.schedule_unique(close_game, 2.0)
        else:
            clock.schedule_unique(update_timer, 1.0)

def close_game(): print("Closing game.."); quit()

def on_mouse_down(pos):
    global score, game_over
    if apple.collidepoint(pos):
        score += 1
        print(f"Good shot! You hit the moving apple. Your score is {score}. ")
    else:
        print(f"Oops! Game over! You missed the moving apple! Your score was {score}")
        game_over = True
        clock.schedule_unique(close_game, 2.0)

clock.schedule_unique(update_timer, 1.0)
pgzrun.go() 
