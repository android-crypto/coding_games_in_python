from random import choice, randint
import pgzrun  # Import pgzrun to use Pygame Zero functionalities

WIDTH = 800
HEIGHT = 600

# Initialize Actors
bash = Actor("bash")
pineapple = Actor("pineapple")
orange = Actor("orange")
kiwi = Actor("kiwi")
roland = Actor("roland")
actors = [bash, pineapple, orange, kiwi, roland]  # List of all actors

score = 0  # Initialize the score variable

def draw():
    screen.clear()
    for actor in actors:
        actor.draw()

def place_actors():
    for actor in actors:
        actor.pos = (randint(10, WIDTH), randint(10, HEIGHT))

def on_mouse_down(pos):
    global score  # Declare score as global to modify it within the function
    actor_clicked = False  # Flag to track if any actor was clicked
    for actor in actors:
        if actor.collidepoint(pos):
            if actor == bash:
                print("Good shot! You hit the bash!")
            else:
                print(f"Oops! You clicked on the {actor.image} by mistake!")
            place_actors()  # Reset actor position
            actor_clicked = True
            break

    if not actor_clicked:
        print("You missed! Game over!")
        quit()

place_actors()  # Place the actors at random positions initially
pgzrun.go()  # Run the game loop

