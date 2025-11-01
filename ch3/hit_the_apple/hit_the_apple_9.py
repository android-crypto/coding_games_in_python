import pygame, pgzrun, string
from random import randint, choice

# ─── Setup ────────────────────────────────────────────────────────────────
WIDTH, HEIGHT = 800, 600
pygame.mixer.init()
pygame.mixer.music.load("music/music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
hit_sound = pygame.mixer.Sound("sounds/hitapple.wav")
miss_sound = pygame.mixer.Sound("sounds/endapple.wav")

apple = Actor("apple", (randint(50, WIDTH-50), randint(50, HEIGHT-50)))
apple.dx, apple.dy = choice([-3, -2, -1, 1, 2, 3]), choice([-3, -2, -1, 1, 2, 3])
apple.angle = 0

score, remaining_time = 0, 30
paused, game_over, space_pressed = False, False, False
TOP3_FILE = "top3scores_click_the_apple.txt"

rules_text = """
PAUSED - GAME RULES:

- Click the apple by moving the mouse cursor over it and clicking.
- The game will end if you click outside the apple.
- Press SPACE to pause or resume the game.
"""

# ─── Helper Functions ─────────────────────────────────────────────────────
def load_top3():
    try:
        with open(TOP3_FILE) as f: return [line.strip().split(",") for line in f if line]
    except FileNotFoundError:
        return []

def place_apple():
    apple.pos = (randint(50, WIDTH-50), randint(50, HEIGHT-50))

def update_timer():
    global remaining_time, game_over
    if not paused and not game_over:
        remaining_time -= 1
        if remaining_time <= 0:
            game_over = True
            clock.schedule_unique(close_game, 5.0)
        else:
            clock.schedule_unique(update_timer, 1.0)

def close_game(): print("Closing game.."); quit()

# ─── Game Logic ───────────────────────────────────────────────────────────
def update():
    global paused, space_pressed, input_active
    if keyboard.space and not space_pressed and not game_over:
        paused = not paused
        space_pressed = True
        pygame.mixer.music.pause() if paused else pygame.mixer.music.unpause()
        if not paused: clock.schedule_unique(update_timer, 1.0)
    elif not keyboard.space:
        space_pressed = False
    if not paused and not game_over: move_apple()
    if game_over: input_active = True

def move_apple():
    apple.x += apple.dx
    apple.y += apple.dy
    if apple.left < 0 or apple.right > WIDTH: apple.dx *= -1
    if apple.top < 0 or apple.bottom > HEIGHT: apple.dy *= -1
    apple.angle = (apple.angle + 5) % 360

def on_mouse_down(pos):
    global score, game_over
    if not paused and not game_over:
        if apple.collidepoint(pos):
            hit_sound.play()
            score += 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            print(f"Good shot! You hit the moving apple. Your score is {score}. ")
            apple.dx += 1 if apple.dx > 0 else -1
            apple.dy += 1 if apple.dy > 0 else -1
            place_apple()
        else:
            print(f"Oops! Game over! You missed the moving apple! Your score was {score}")
            miss_sound.play()
            game_over = True

def on_key_down(key):
    global initials, input_active
    if input_active:
        if key.name in string.ascii_uppercase and len(initials) < 3:
            initials += key.name
        elif key == keys.BACKSPACE: initials = initials[:-1]
        elif key == keys.RETURN and len(initials) == 3:
            add_to_top3(initials, score)
            input_active = False
            clock.schedule_unique(close_game, 3.0)

def draw():
    screen.clear()
    if not game_over:
        apple.draw()
        screen.draw.text(f"Score: {score}", topright=(WIDTH-10, 10), fontsize=30)
        screen.draw.text(f"Time: {remaining_time}s", topleft=(10, 10), fontsize=30)
        if paused:
            screen.draw.filled_rect(Rect(100,100,WIDTH-200,HEIGHT-200),(0,0,0,180))
            screen.draw.textbox(rules_text, Rect(150,150,WIDTH-300,HEIGHT-300), color="white")
    else:
        screen.fill("black")
        screen.draw.text("Game Over", center=(WIDTH//2, 100), fontsize=60)
# ─── Start Game ───────────────────────────────────────────────────────────
place_apple()
clock.schedule_unique(update_timer, 1.0)
pgzrun.go()
