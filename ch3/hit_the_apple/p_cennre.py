import pgzrun

WIDTH = 800
HEIGHT = 600

apple = Actor("apple")
apple.pos = (WIDTH // 2, HEIGHT // 2)

def draw():
    screen.clear()
    apple.draw()

# Start the Pygame Zero loop
pgzrun.go()
