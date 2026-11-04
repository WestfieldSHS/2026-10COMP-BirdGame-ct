# start modules
from cmath import pi
from random import randint
import pgzrun
import sys
# create constants
WIDTH = 800
HEIGHT = 600
gameOver = False
score = 0
# print welcome
print("The game is about to start!")
# make background
background = Actor("day")
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
        
pipe_1 = Pipes(666, 400, 220)
pipe_2 = Pipes(932, 280, 220)
pipe_3 = Pipes(1198, 415, 220)

pipeslist = [pipe_1, pipe_2, pipe_3]

def random_centre():
    centre = randint(200, 400)
    return centre
def random_gap():
    gap = randint(180, 240)
    return gap

# draw everything to screen
def draw():
    global gameOver, score
    if gameOver == False:

        # draw background
        background.draw()
        # draw characters
        bird.draw()
        for pipe in pipeslist:
            pipe.top.draw()
            pipe.bottom.draw()
        screen.draw.text(f"{score}", center=(400,50), fontsize = 100)
    else:
        screen.fill((0,0,0))
        screen.draw.text("Game Over!", center = (400,300), fontsize = 60)
        screen.draw.text(f"Score is:{score}",center=(400,450), fontsize = 30)
# update everything
def update():
    global gameOver, score
    if gameOver == False:
        
        
        # update bird
        bird.y = bird.y + 2.5
        # update pipes
        for pipe in pipeslist:
            if pipe.top.x < -44:
                score += 1
                pipe.top.x = 740
                pipe.bottom.x = 740
                gap = random_gap()
                centre = random_centre()
                pipe.top.y = centre - ((HEIGHT/2)+(gap/2))
                pipe.bottom.y = centre + ((HEIGHT/2)+(gap/2))
            pipe.top.x -= 3
            pipe.bottom.x -= 3
           
        # bird hits bottom of screen
        if bird.y > HEIGHT:
            print("Game Over!")
            sys.exit()
        # bird hits pipes
        for pipe in pipeslist:
            if pipe.top.colliderect(bird) or pipe.bottom.colliderect(bird):
                print("Hit!")
                print("Game Over!")
                gameOver = True
            # sys.exit()
        
def on_mouse_down():
    bird.y -= 50
# runs everything
pgzrun.go()