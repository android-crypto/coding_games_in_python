coin.pos = 200, 200
def draw():
screen.fill("green")
fox.draw()
coin.draw()
screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))