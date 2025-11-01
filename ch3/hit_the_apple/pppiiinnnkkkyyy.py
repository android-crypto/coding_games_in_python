import pgzrun

WIDTH = 800
HEIGHT = 600

pinky = Actor("pinky")
pinky2 = Actor("pinky2")
pinky0 = Actor("pinky0")
pinky19 = Actor("pinky19")
pinky7 = Actor("pinky7")

def draw():
    screen.clear()
    pinky.draw()
    pinky2.draw()
    pinky0.draw()
    pinky19.draw()
    pinky7.draw()

def place_pinky_center():
    pinky.x = WIDTH // 2
    pinky.y = HEIGHT // 2

def place_pinky2_top_right():
    pinky2.x = WIDTH - pinky2.width // 2
    pinky2.y = pinky2.height // 2

def place_pinky0_top_left():
    pinky0.x = pinky0.width // 2
    pinky0.y = pinky0.height // 2

def place_pinky19_bottom_right():
    pinky19.x = WIDTH - pinky19.width // 2
    pinky19.y = HEIGHT - pinky19.height // 2

def place_pinky7_bottom_left():
    pinky7.x = pinky7.width // 2
    pinky7.y = HEIGHT - pinky7.height // 2

# Initially place the images in their respective positions
place_pinky_center()
place_pinky2_top_right()
place_pinky0_top_left()
place_pinky19_bottom_right()
place_pinky7_bottom_left()

