import random
class Car(object):
# The Constructor is defined with arguments.
    def __init__(self, c, xpos, ypos, xspeed, yspeed, L, B, l, b):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.L = L
        self.B = B
        self.l = l
        self.b = b

    def display(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, self.L, self.B);
        rect(self.xpos-(self.L)/2, self.ypos-(self.B)/2-(self.b)/2, self.l, self.b)
        rect(self.xpos-(self.L)/2, self.ypos+(self.B)/2+(self.b)/2, self.l, self.b)
        line(self.xpos+(self.L)/2, self.ypos+(self.B)/6, self.xpos+(self.L)/2+(self.B)/2, self.ypos+(self.B)/2)
        line(self.xpos+(self.L)/2, self.ypos-(self.B)/6, self.xpos+(self.L)/2+(self.B)/2, self.ypos-(self.B)/2)

    def drive(self):
        self.xpos = self.xpos + self.xspeed
        self.ypos = self.ypos + self.yspeed
        if self.xpos > width or self.xpos <=0:
            self.xspeed *= -1
        if self.ypos > height or self.ypos <=0:
            self.yspeed *= -1
            
            
            
#color,xpos,ypos,xspeed,yspeed,L,B,l,b
d=random.uniform(2,10)
c=color(0)
D=500
n=int(random.uniform(1,50))
objs = list()
for i in range(n):
    objs.append(Car(color(random.uniform(0,255), random.uniform(0,255), random.uniform(0,255)), random.uniform(0,2*D), random.uniform(0,D), random.uniform(1,10), random.uniform(1,10), 8*d, 4*d, 2*d, d))

def setup():
    size(2*D,D)

def draw(): 
  background(100,100,0)
  for i in range(n):
      objs[i].drive()
      objs[i].display()
