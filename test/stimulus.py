import math
import random
class stimulus(object):
    def __init__(self, img, x, y, xspeed, yspeed):
        self.xspeed = xspeed    # horizontal velocity
        self.yspeed = yspeed    # vertical velocity
        # position of stimulus: (x,y)
        self.x = x
        self.y = y
        self.img = img   # stimulus as image

    # to display stimulus
    def display(self):
        stroke(0)
        image(self.img,self.x-40,self.y-30,80,60)

    def location(self):
        return self.x,self.y
    # takes care of vehicle movement
    def move(self):
        self.x = self.x + self.xspeed
        self.y = self.y + self.yspeed
        # to make the stimuli rebound from boundaries
        if self.x > width or self.x <=0:
            self.xspeed *= -1
        if self.y > height or self.y <=0:
            self.yspeed *= -1
