import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 600

score = 0
game_over = False

fox = Actor("fox")
fox.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200

quarter = Actor("quarter")
quarter.pos = 150, 150

realdime = Actor("realdime")
realdime.pos = 169, 100

kennedy = Actor("kennedy")
kennedy.pos = 149, 108

def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    realdime.draw()
    quarter.draw()
    kennedy.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))

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

def time_up():
    
    global game_over
    game_over = True

def update():
    global score

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


clock.schedule(time_up, 100.0)
place_coin()
place_quarter()
place_realdime()
place_kennedy()

pgzrun.go()
