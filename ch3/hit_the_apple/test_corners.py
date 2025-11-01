import pgzrun

WIDTH = 800
HEIGHT = 600

pinky = Actor("pinky")
pinky = Actor("pinky")
pinky = Actor("pinky")
pinky = Actor("pinky")
pinky = Actor("pinky")

def draw():
    screen.clear()
    pinky.draw()
    pinky.draw()
    pinky.draw()
    pinky.draw()
    pinky.draw()

def place_pinky_center():
    pinky.x = WIDTH // 2
    pinky.y = HEIGHT // 2

def place_pinky_top_right():
    pinky.x = WIDTH - pinky.width // 2
    pinky.y = pinky.height // 2

def place_pinky_top_left():
    pinky.x = pinky.width // 2
    pinky.y = pinky.height // 2

def place_pinky_bottom_right():
    pinky.x = WIDTH - pinky.width // 2
    pinky.y = HEIGHT - pinky.height // 2

def place_pinky_bottom_left():
    pinky.x = pinky.width // 2
    pinky.y = HEIGHT - pinky.height // 2

# Initially place the images in their respective positions
place_pinky_center()
place_pinky_top_right()
place_pinky_top_left()
place_pinky_bottom_right()
place_pinky_bottom_left()

