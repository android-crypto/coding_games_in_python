import pgzrun

WIDTH = 800
HEIGHT = 600

pinky = Actor("pinky")
pinky.pos = (WIDTH // 2, HEIGHT // 2)

def draw():
    screen.clear()
    pinky.draw()

# Start the Pygame Zero loop
pgzrun.go()