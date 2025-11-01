from random import choice, randint
import pgzrun  # Import pgzrun to use Pygame Zero functionalities

WIDTH = 800
HEIGHT = 600

# Initialize Actors
apple = Actor("apple")
pineapple = Actor("pineapple")
orange = Actor("orange")
actors = [apple, pineapple, orange]  # List of all actors

rules_text = """
PAUSED - GAME RULES:

- Click the apple by moving the mouse cursor over it and clicking.
- The game will end if you click outside the apple.
- Press SPACE to pause or resume the game.
"""

score = 0  # Initialize the score variable

def draw():
    screen.clear()
    for actor in actors:
        actor.draw()
    print("Score:", score)  # Print the score

def place_actors():
    for actor in actors:
        actor.pos = (randint(10, WIDTH), randint(10, HEIGHT))

def on_mouse_down(pos):
    global score  # Declare score as global to modify it within the function
    actor_clicked = False  # Flag to track if any actor was clicked
    for actor in actors:
        if actor.collidepoint(pos):
            if actor == apple:
                print("Good shot! You hit the apple!"); sounds.hitapple.play(); score += 1
            else:
                print(f"Oops! You clicked on the {actor.image} by mistake!"); sounds.laser.play(); place_actors(); actor_clicked = True
    if not actor_clicked:
        print("You missed! Game over!")
place_actors()  # Place the actors at random positions initially
pgzrun.go()  # Run the game loop
