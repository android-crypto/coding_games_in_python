import pgzrun

# Set the width and height of the window
WIDTH = 800
HEIGHT = 600

# Load the pinky0 actor
pinky0 = Actor("pinky0")

# Position the apple in the top-left corner
pinky0.pos = (40, 55)

def draw():
    # Clear the screen
    screen.clear()
    # Draw the pinky0 actor
    pinky0.draw()

# Start the Pygame Zero loop
pgzrun.go()
