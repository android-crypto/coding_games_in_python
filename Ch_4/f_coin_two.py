import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 600

score = 0
game_over = False

fox = Actor("fox")
fox.pos = 100, 100

hedgehog = Actor("hedgehog")
hedgehog.pos = 100, 100

hedgeho = Actor("hedgeho")
hedgeho.pos = 100, 100


coin = Actor("coin")
coin.pos = 200, 200

quarter = Actor("quarter")
quarter.pos = 150, 150

realdime = Actor("realdime")
realdime.pos = 169, 100

kennedy = Actor("kennedy")
kennedy.pos = 149, 108

koin = Actor("koin")
koin.pos = 165, 105

def draw():
    screen.fill("white")
    fox.draw()
    hedgehog.draw()
    hedgeho.draw()
    coin.draw()
    realdime.draw()
    quarter.draw()
    kennedy.draw()
    koin.draw()
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

def place_koin():
    koin.x = randint(20, WIDTH - 20)
    koin.y = randint(20, HEIGHT - 20)

def time_up():
    
    global game_over
    game_over = True

def update():
    global score

    if not game_over:
        if keyboard.a:
            fox.x -= 4
        elif keyboard.d:
            fox.x += 4
        elif keyboard.w:
            fox.y -= 4
        elif keyboard.s:
            fox.y += 4

        if keyboard.j:
            hedgehog.x -= 15
        elif keyboard.l:
            hedgehog.x += 15
        elif keyboard.i:
            hedgehog.y -= 15
        elif keyboard.k:
            hedgehog.y += 15

        if keyboard.left:
            hedgeho.x -= 50
        elif keyboard.right:
            hedgeho.x += 50
        elif keyboard.up:
            hedgeho.y -= 50
        elif keyboard.down:
            hedgeho.y += 50


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

        if hedgehog.colliderect(coin):
            score += 1
            place_coin()

        if hedgehog.colliderect(quarter):
            score += 25
            place_quarter()

        if hedgehog.colliderect(realdime):
            score += 10
            place_realdime()

        if hedgehog.colliderect(kennedy):
            score += 50
            place_kennedy()

        if hedgehog.colliderect(koin):
            score += 100
            place_koin()

        if hedgeho.colliderect(coin):
            score += 1
            place_coin()

        if hedgeho.colliderect(quarter):
            score += 25
            place_quarter()

        if hedgeho.colliderect(realdime):
            score += 10
            place_realdime()

        if hedgeho.colliderect(kennedy):
            score += 50
            place_kennedy()

        if hedgeho.colliderect(koin):
            score += 100
            place_koin()


clock.schedule(time_up, 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999.0)
place_coin()
place_quarter()
place_realdime()
place_kennedy()
place_koin()

pgzrun.go()
