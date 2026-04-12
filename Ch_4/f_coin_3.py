import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 600

score = 0
paused = False
game_over = False
remaining_time = 60
space_pressed = False

fox = Actor("fox")
fox.pos = 100, 100

coin = Actor("coin")
quarter = Actor("quarter")
realdime = Actor("realdime")
kennedy = Actor("kennedy")
koin = Actor("koin")

rules_text = """
PAUSED - GAME RULES:
- Acquire the most score
- Press SPACE to pause or resume the game.
"""


def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    realdime.draw()
    quarter.draw()
    kennedy.draw()
    koin.draw()
    screen.draw.text(f"Score: {score}", topright=(WIDTH-10, 10), fontsize=30)
    screen.draw.text(f"Time: {remaining_time}s", topleft=(10, 10), fontsize=30)
    if paused:
        screen.draw.filled_rect(Rect(100,100,WIDTH-200,HEIGHT-200),(0,0,0,180))
        screen.draw.textbox(rules_text.strip(), Rect(150, 150, WIDTH - 300, HEIGHT - 300), color="white", align="left")
    if game_over:
        screen.fill("pink")
        if score >= 100:
            screen.draw.text("You Win!", topleft=(100, 200), fontsize=60, color="black")
        else:
            screen.draw.text("Game Over", topleft=(100, 200), fontsize=60, color="black")

def place_coin():
    coin.x = randint(20, WIDTH - 20)
    coin.y = randint(20, HEIGHT - 20)

def place_quarter():
    quarter.x = randint(20, WIDTH - 20)
    quarter.y = randint(20, HEIGHT - 20)

def place_realdime():
    realdime.x = randint(20, WIDTH - 20)
    realdime.y = randint(20, HEIGHT - 20)

def place_kennedy():
    kennedy.x = randint(20, WIDTH - 20)
    kennedy.y = randint(20, HEIGHT - 20)

def place_koin():
    koin.x = randint(20, WIDTH - 20)
    koin.y = randint(20, HEIGHT - 20)

def update_timer():
    global remaining_time, game_over
    remaining_time -= 1
    if remaining_time <= 0:
        game_over = True
        print(f"Time's up! Your final score was {score}.")
        clock.schedule_unique(close_game, 3.0)
    else:
        clock.schedule_unique(update_timer, 1.0)

def close_game(): print("Closing game.."); quit()

def update():
    global paused, space_pressed, score, game_over
    # allow pause/suesm toggle always when not game_over
    if keyboard.space and not space_pressed and not game_over:
        paused = not paused
        space_pressed = True
        # stop all other updateds if puased or game is over
        if paused or game_over: 
            return # skip any game logic
        else:
            clock.schedule_unique(update_timer, 1.0)
    elif not keyboard.space:
        space_pressed = False

    if not game_over:
        if keyboard.left:
            fox.x -= 6
        elif keyboard.right:
            fox.x += 6
        elif keyboard.up:
            fox.y -= 6
        elif keyboard.down:
            fox.y += 6

        if fox.colliderect(coin):
            score += 1
            place_coin()

        if fox.colliderect(quarter):
            score += 25
            place_quarter()

        if fox.colliderect(realdime):
            score += 10
            place_realdime()

        if fox.colliderect(kennedy):
            score += 50
            place_kennedy()

        if fox.colliderect(koin):
            score += 100
            place_koin()


place_coin()
place_quarter()
place_realdime()
place_kennedy()
place_koin()

clock.schedule_unique(update_timer, 1.0)
pgzrun.go()
