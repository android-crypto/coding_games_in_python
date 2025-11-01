import pgzrun

WIDTH = 800
HEIGHT = 600

evil_android = Actor("evil_android")

def draw():
	screen.clear()
	evil_android.draw()

pgzrun.go()