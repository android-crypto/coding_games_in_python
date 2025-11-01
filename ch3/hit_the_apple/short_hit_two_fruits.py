from random import choice, randint
import pgzrun

WIDTH = 800
HEIGHT = 600

# Initialize Actors
actors = [Actor("apple"), Actor("pineapple"), Actor("orange"), Actor("kiwi"), Actor("roland")]
moving_actors = [actors[0], actors[2]]  # apple and orange

score = 0

def draw():
    screen.clear()
    for actor in actors:
        actor.draw()
    print("Score:", score)

def place_actors():
    for actor in moving_actors:
        actor.pos = (randint(10, WIDTH), randint(10, HEIGHT))

def on_mouse_down(pos):
    global score
    for actor in actors:
        if actor.collidepoint(pos):
            if actor.image == "apple":
                print("Good shot! You hit the apple!")
                score += 1
            else:
                print(f"Oops! You clicked on the {actor.image} by mistake!")
            place_actors()
            return  # Exit after handling click

    print("You missed! Game over!")
    quit()

place_actors()
pgzrun.go()
