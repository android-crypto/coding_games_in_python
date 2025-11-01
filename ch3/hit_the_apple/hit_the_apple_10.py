import pygame, pgzrun, choice
from random import randint
# Import pgzrun to use Pygame Zero functionalities   
game_over = False

score, remaining_time = 0, 60


  
WIDTH = 800
HEIGHT = 600

pygame.mixer.init()
pygame.mixer.music.load("music/music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
hit_sound = pygame.mixer.Sound("sounds/hitapple.wav")
miss_sound = pygame.mixer.Sound("sounds/endapple.wav")

paused = False
space_clicked = False

# Initialize Actors
apple = Actor("apple")
pineapple = Actor("pineapple")
orange = Actor("orange")
actors = [apple, pineapple, orange]  # List of all actors

rules_text = """
PAUSED - GAME RULES:

- Click the apple by moving the mouse cursor over it and clicking.
- The game will end if you click outside the apple.
- Press SPACE to pause or resume the game.
"""


def draw():
    screen.clear()
    for actor in actors:
        actor.draw()
        screen.draw.text(f"Score: {score}", topright=(WIDTH-10, 10), fontsize=30)
        screen.draw.text(f"Time: {remaining_time}s", topleft=(10, 10), fontsize=30)
    if paused:
        screen.draw.filled_rect(Rect(100,100,WIDTH-200,HEIGHT-200),(0,0,0,180))
        screen.draw.textbox(rules_text, Rect(150,150,WIDTH-300,HEIGHT-300), color="white")
    if game_over:
        screen.fill("black")
        screen.draw.text("Game Over", center=(WIDTH//2, 100), fontsize=60)

def place_apple():
    apple.pos = (randint(10, WIDTH), randint(-10, HEIGHT))

def place_orange():
    orange.pos = (randint(10, WIDTH), randint(-10, HEIGHT))

def place_pineapple():
    pineapple.pos = (randint(10, WIDTH), randint(-10, HEIGHT))

def close_game(): print("Closing game.."); quit()

def update_timer():
    global remaining_time, game_over
    if not paused and not game_over:
        remaining_time -= 1
        if remaining_time <= 0:
            game_over = True
            clock.schedule_unique(close_game, 5.0)
            print(f"your score was {score}")
        else:
            clock.schedule_unique(update_timer, 1.0)
    else:
        clock.schedule_unique(update_timer, 1.0)


def update():
    global paused, space_clicked
    if keyboard.space and not space_clicked and not game_over:
        pygame.mixer.music.pause() if paused else pygame.mixer.music.unpause
        paused = not paused
        space_clicked = True
    elif not keyboard.space:
        space_clicked = False
    if paused or game_over:
        return
def move_apple():
    apple.x += apple.dx
    apple.y += apple.dy
    if apple.left < 0 or apple.right > WIDTH: apple.dx *= -1
    if apple.top < 0 or apple.bottom > HEIGHT: apple.dy *= -1
    apple.angle = (apple.angle + 5) % 360
    
def move_orange():
    orange.x += orange.dx
    orange.y += orange.dy
    if orange.left < 0 or orange.right > WIDTH: orange.dx *= -1
    if orange.top < 0 or orange.bottom > HEIGHT: orange.dy *= -1
    orange.angle = (orange.angle + 5) % 360

def move_pineapple():
    pineapple.x += pineapple.dx
    pineapple.y += pineapple.dy
    if pineapple.left < 0 or pineapple.right > WIDTH: pineapple.dx *= -1
    if pineapple.top < 0 or pineapple.bottom > HEIGHT: pineapple.dy *= -1
    pineapple.angle = (pineapple.angle + 5) % 360

def on_mouse_down(pos):
    global score
    if paused or game_over:
        return
    actor_clicked = False  # Flag to track if any actor was clicked 
    for actor in actors:
        if actor.collidepoint(pos):
            if actor == apple:
                print("Good shot! You hit the apple!")
                hit_sound.play()
                score += 1
                place_apple()
            elif actor == pineapple:
                print("miss ya hited da pinapol")
                hit_sound.play()
                place_pineapple()
            elif actor == orange:
                print("miss ya hited da ohrage")
                hit_sound.play()
                place_orange()  # Reset actor position
            actor_clicked = True
            break

        if not actor_clicked:
            print("You missed! Game over!")
            miss_sound.play()
            clock.schedule_unique(close_game, 3.0)

place_apple()
place_orange()
place_pineapple()# Place the actors at random positions initially
clock.schedule_unique(update_timer, 1.0)
pgzrun.go()  # Run the game loop
