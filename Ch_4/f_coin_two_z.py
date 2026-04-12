import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 600

fox_score = 0
hedgehog_score = 0
hedgeho_score = 0
game_over = False
winner = None

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

cons = [coin, quarter, realdime, kennedy, koin]

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
    screen.draw.text("fox usd: " + str(fox_score), color="black", topleft=(10, 10))
    screen.draw.text("hedegehog usd: " + str(hedgehog_score), color="black", topleft=(10, 30))
    screen.draw.text("hedgeho usd: " + str(hedgeho_score), color="black", topleft=(10, 50))
    if game_over:
        screen.fill("pink")
        if winner == "fox":
            screen.draw.text("fox Wins!", topleft=(100, 200), fontsize=60, color="black")
        if winner == "hedgehog":
            screen.draw.text("hedgehog Wins!", topleft=(100, 200), fontsize=60, color="black")
        if winner == "hedgeho":
            screen.draw.text("hedegeho Wins!", topleft=(100, 200), fontsize=60, color="black")

def place_cons():
    for actor in cons:  
        actor.pos = (randint(10, WIDTH - 10), randint(10, HEIGHT - 10))

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
    global fox_score, hedgehog_score, hedgeho_score
 

 
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
            fox_score += 10
            place_cons()

        if fox.colliderect(quarter):
            fox_score += 0.25
            place_cons()

        if fox.colliderect(realdime):
            fox_score += 0.10
            place_cons()

        if fox.colliderect(kennedy):
            fox_score += 0.50
            place_cons()

        if fox.colliderect(koin):
            fox_score += 1
            place_cons()

        if hedgehog.colliderect(coin):
            fox_score += 10
            place_cons()

        if hedgehog.colliderect(quarter):
            hedgehog_score += 0.25
            place_cons()

        if hedgehog.colliderect(realdime):
            hedgehog_score += 0.10
            place_cons()

        if hedgehog.colliderect(kennedy):
            hedgehog_score += 0.50
            place_cons()

        if hedgehog.colliderect(koin):
            hedgehog_score += 1
            place_cons()

        if hedgeho.colliderect(coin):
            hedgeho_score += 10
            place_cons()

        if hedgeho.colliderect(quarter):
            hedgeho_score += 0.25
            place_cons()

        if hedgeho.colliderect(realdime):
            hedgeho_score += 0.10
            place_cons()

        if hedgeho.colliderect(kennedy):
            hedgeho_score += 0.50
            place_cons()

        if hedgeho.colliderect(koin):
            hedgeho_score += 1
            place_cons()


clock.schedule(time_up, 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999.0)
place_coin()
place_quarter()
place_realdime()
place_kennedy()
place_koin()

pgzrun.go()
