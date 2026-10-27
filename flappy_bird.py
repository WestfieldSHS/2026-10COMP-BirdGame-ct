# start modules
from cmath import pi

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
        self.top = Actor("top")
        self.top.y = centre - ((HEIGHT/2)+(gap/2))
        self.top.x = x
        self.bottom = Actor("bottom")
        self.bottom.y = centre + ((HEIGHT/2)+(gap/2))
        self.bottom.x = x
        
pipeslist = [
    Pipes(266, 400, 220),
    Pipes(532, 180, 220),
    Pipes(798, 415, 220)

]

# draw everything to screen
def draw():
    
    
    # draw background
    background.draw()
    # draw characters
    bird.draw()
# update everything
def update():
    bird.y = bird.y + 1
    # update bird

    # update pipes
    for pipe in pipeslist:
        self.top.x += 5
        self.bottom.x += 5
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