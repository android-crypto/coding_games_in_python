import pgzrun

WIDTH = 800
HEIGHT = 600

pinky = Actor("pinky")
superawesomecorn = Actor("superawesomecorn")
penguin = Actor("penguin")
sebastian = Actor("sebastian")
weirdodude = Actor("weirdodude")

def draw():
    screen.clear()
    pinky.draw()
    superawesomecorn.draw()
    penguin.draw()
    sebastian.draw()
    weirdodude.draw()

def place_pinky_center():
    pinky.x = WIDTH // 2
    pinky.y = HEIGHT // 2

def place_superawesomecorn_top_right():
    superawesomecorn.x = WIDTH - superawesomecorn.width // 2
    superawesomecorn.y = superawesomecorn.height // 2

def place_penguin_top_left():
    penguin.x = penguin.width // 2
    penguin.y = penguin.height // 2

def place_sebastian_bottom_right():
    sebastian.x = WIDTH - sebastian.width // 2
    sebastian.y = HEIGHT - sebastian.height // 2

def place_weirdodude_bottom_left():
    weirdodude.x = weirdodude.width // 2
    weirdodude.y = HEIGHT - weirdodude.height // 2

# Initially place the images in their respective positions
place_pinky_center()
place_superawesomecorn_top_right()
place_penguin_top_left()
place_sebastian_bottom_right()
place_weirdodude_bottom_left()

pgzrun.go()