import pgzrun

# Define screen dimensions
WIDTH = 800
HEIGHT = 600

# Create actor instances

pineapple = Actor("pineapple")

# List of actors for easy management
actors = [pineapple]




# Position the other fruits in fixed positions

pineapple.pos = (pineapple.width // 2 + 50, pineapple.height // 2 + 50)