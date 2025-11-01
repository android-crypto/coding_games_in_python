from random import choice, randint
import pgzrun  # Import pgzrun to use Pygame Zero functionalities

WIDTH = 800
HEIGHT = 600

# Initialize Actors
apple = Actor("apple")
penguin = Actor("penguin")
superawesomecorn = Actor("superawesomecorn")
sebastian = Actor("sebastian")
pinky = Actor("pinky")
pineapple = Actor("pineapple")
orange = Actor("orange")
kiwi = Actor("kiwi")
roland = Actor("roland")
actors = [apple, pineapple, orange, kiwi, roland, sebastian, pinky, superawesomecorn, penguin]  # List of all actors

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
            if actor == pinky:
                print("jwane jwon sin wagwandah")
                score += 1
            else:
                print(f"aw {actor.image} man")
            place_actors()  # Reset actor position
            actor_clicked = True
            break

    if not actor_clicked:
        print("You missed! Game over!")
        quit()

place_actors()  # Place the actors at random positions initially
pgzrun.go()  # Run the game loop
