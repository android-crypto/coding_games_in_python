from random import randint
import pgzrun

# Set up screen dimensions
WIDTH = 800
HEIGHT = 600

# Initialize Actors
apple = Actor("apple")
pineapple = Actor("pineapple")
orange = Actor("orange")
kiwi = Actor("kiwi")
roland = Actor("roland")
evil_android = Actor("evil_android")

actors = [apple, pineapple, orange, kiwi, roland, evil_android]

score = 0  # Initialize score variable
time_left = 30  # Set initial time to 30 seconds

def draw():
    screen.clear()
    for actor in actors:
        actor.draw()
    screen.draw.text(f"Score: {score}", (10, 10), color="white")
    screen.draw.text(f"Time left: {time_left}s", (WIDTH - 150, 10), color="white")  # Display timer

def place_actors():
    for actor in actors:
        actor.pos = (randint(10, WIDTH - 10), randint(10, HEIGHT - 10))

def update_timer():
    global time_left
    if time_left > 0:
        time_left -= 1  # Decrease time by 1 second
    else:
        print("Time's up! Game over!")
        quit()

def on_mouse_down(pos):
    global score
    actor_clicked = False
    for actor in actors:
        if actor.collidepoint(pos):
            if actor == apple:
                print("Good shot! You hit the apple!")
                score += 99999999999999999999999999999999999999999999
            elif actor == evil_android:
                print("Oh no! You clicked on the evil Android!")
                score -= 1
            else:
                print(f"Oops! You clicked on the {actor.image} by mistake!")
            place_actors()
            actor_clicked = True
            break

    if not actor_clicked:
        print("You missed! Game over!")
        quit()

# Schedule the timer to update every second
clock.schedule_interval(update_timer, 1.0)

place_actors()  # Place the actors at random positions initially
pgzrun.go()  # Run the game loop
