import random
import math
class stimulus(object):

    def __init__(self, img, x, y, xspeed, yspeed):
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.x = x
        self.y = y
        self.img = img

    def display(self):
        stroke(0)
        image(self.img,self.x-40,self.y-30,80,60)

    def location(self):
        return self.x,self.y

    def drive(self):
        self.x = self.x + self.xspeed
        self.y = self.y + self.yspeed
        if self.x > width or self.x <=0:
            self.xspeed *= -1
        if self.y > height or self.y <=0:
            self.yspeed *= -1

#m: no. of stimuli
m = int(random.uniform(1,10))
img = loadImage("cry.jpg")
D = 600
stim = list()
for i in range(m):
    stim.append(stimulus(img, random.uniform(0,2*D), random.uniform(0,D), random.uniform(5,10),random.uniform(5,10)))


class vehicle(object):
# The Constructor is defined with arguments.
    def __init__(self, xpos, ypos, L, B, l, b):
        #self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.L = L
        self.B = B
        self.l = l
        self.b = b


 #   def rotates(self,x,y,cosine,sine):
  #      return x*cosine-y*sine,x*sine+y*cosine

    def display(self):
        stroke(0)
        c = color(int(255*(1-math.exp(-self.total_activation()))))
        #c=color(random.uniform(0,255))
        fill(c)
        rectMode(CENTER)
    #    self.xpos,self.ypos = self.rotates(self.xpos,self.ypos,(x-self.xpos)/self.distance(),(y-self.ypos)/self.distance())
        rect(self.xpos, self.ypos, self.L, self.B);
        rect(self.xpos-(self.L)/2, self.ypos-(self.B)/2-(self.b)/2, self.l, self.b)
        rect(self.xpos-(self.L)/2, self.ypos+(self.B)/2+(self.b)/2, self.l, self.b)
        line(self.xpos+(self.L)/2, self.ypos+(self.B)/6, self.xpos+(self.L)/2+(self.B)/2, self.ypos+(self.B)/2)
        line(self.xpos+(self.L)/2, self.ypos-(self.B)/6, self.xpos+(self.L)/2+(self.B)/2, self.ypos-(self.B)/2)

    def location(self):
        return self.xpos,self.ypos

    def distance(self,i):
        x,y =stim[i].location()
        return sqrt((x-self.xpos)**2+(y-self.ypos)**2)

    def activation(self,i):
        k=1000
        k1=1
        k2=.01
        r = self.distance(i)
        return k/(k1+k2*r*r)

    def total_activation(self):
        total=0
        for i in range(m):
            total+=self.activation(i)
        return total


    def drive(self,xspeed,yspeed):
        for i in range(m):
            x,y =stim[i].location()
            xspeed += self.activation(i)*abs(x-self.xpos)/self.distance(i)
            yspeed += self.activation(i)*abs(y-self.ypos)/self.distance(i)

        if self.xpos > width or self.xpos <=0:
            self.xpos = 0
        if self.ypos > height or self.ypos <=0:
            self.ypos = 0

        self.xpos = self.xpos + xspeed
        self.ypos = self.ypos + yspeed

#color,xpos,ypos,L,B,l,b
d=3
c=color(250,0,250)
n=int(random.uniform(1,500))
objs = list()
for i in range(n):
    objs.append(vehicle(random.uniform(0,2*D), random.uniform(0,D), 8*d, 4*d, 2*d, d))

def setup():
    size(2*D,D)

def draw():
  background(100,100,0)
  for i in range(m):
    stim[i].display()
    stim[i].drive()

  for i in range(n):
      objs[i].drive(0,0)
      objs[i].display()
