import pgzrun 

WIDTH = 800
HEIGHT = 600

evil_android = Actor("evil_android")

def draw():
	screen.clear()
	evil_android.pos = (705,50) #set the position of the evil_android
	evil_android.draw()

pgzrun.go()

