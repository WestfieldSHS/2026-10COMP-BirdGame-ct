# start modules
import pgzrun
import sys
# create constants
WIDTH = 800
HEIGHT = 600
# print welcome
print("The game is about to start!")
# make background
background = Actor("bg")
background.x = 400
background.y = 300
# make bird
bird = Actor("bird")
bird.y = 300
bird.x = 160
# make pipes
class Pipes():
    def __init__(self, x, centre, gap):
        self.x  = x
        pipe = Pipes(x, centre)
        pipe.x = 6
pipeslist = [
    Pipes(266, 400, 220),
    Pipes(532, 180, 220),
    Pipes(798, 415, 220)

]

# draw everything to screen
def draw():
    nin
    
    # draw background

    # draw characters

# update everything
def update():
    bird.y = bird.y + 1
    # update bird

    # update pipes
for pipe in pipeslist:
    pipe = pipe + 5
    # bird hits bottom of screenq
    if background.y > HEIGHT:
        print("Game Over!")
        sys.exit()
    # bird hits pipes
if bird.colliderect(pipe):
    print("Hit!")
# moving
def on_mouse_down():
    bird.y - 50
# runs everything
pgzrun.go()