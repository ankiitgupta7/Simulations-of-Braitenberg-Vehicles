import random
import math
import stimulus

#m: no. of stimuli
m = int(random.uniform(1,2))
img = loadImage("cry.jpg")
D = 600
stim = list()
for i in range(m):
    stim.append(stimulus.stimulus(img, random.uniform(0,2*D), random.uniform(0,D), random.uniform(0,10), random.uniform(0,10)))
    #stim.append(stimulus.stimulus(img, 600, 300, 0, 0))


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
    #    print(self.xpos, self.ypos)
        vx,vy = self.drive(0,0)
        v = sqrt(vx**2+vy**2)
        c = color(int(255*(1-math.exp(-v))))
        #c=color(random.uniform(0,255))
        fill(c)
        rectMode(CENTER)
    #    self.xpos,self.ypos = self.rotates(self.xpos,self.ypos,(x-self.xpos)/self.distance(),(y-self.ypos)/self.distance())
        rect(self.xpos, self.ypos, self.L, self.B);
        s1x,s1y,s2x,s2y = self.sensor_pos()
        if(vx>=0):
            rect(self.xpos-(self.L)/2, self.ypos-(self.B)/2-(self.b)/2, self.l, self.b)
            rect(self.xpos-(self.L)/2, self.ypos+(self.B)/2+(self.b)/2, self.l, self.b)
            line(self.xpos+(self.L)/2, self.ypos+(self.B)/6, s1x, s1y)
            line(self.xpos+(self.L)/2, self.ypos-(self.B)/6, s2x, s2y)
        else :
            rect(self.xpos+(self.L)/2, self.ypos-(self.B)/2-(self.b)/2, self.l, self.b)
            rect(self.xpos+(self.L)/2, self.ypos+(self.B)/2+(self.b)/2, self.l, self.b)
            line(self.xpos-(self.L)/2, self.ypos+(self.B)/6, s1x, s1y)
            line(self.xpos-(self.L)/2, self.ypos-(self.B)/6, s2x, s2y)

    def sensor_pos(self):
        vx,vy = self.drive(0,0)
        if(vx>=0):
            return self.xpos+(self.L)/2+(self.B)/2, self.ypos+(self.B)/2, self.xpos+(self.L)/2+(self.B)/2, self.ypos-(self.B)/2
        else :
            return self.xpos-(self.L)/2-(self.B)/2, self.ypos+(self.B)/2, self.xpos-(self.L)/2-(self.B)/2, self.ypos-(self.B)/2

    # calculates Euclidean distance between (x,y) : sensor  and (sx,sy) : stimulus
    def distance(self,i,x,y):
        sx,sy = stim[i].location()
        return sqrt((x-sx)**2+(y-sy)**2)

    # i : activation due to i'th stimulus
    # index : refers to index of sensor (in case of multiple)
    def activation(self,i,index):
        k=.01
        k1=1
        k2=.0001
        if(index==1):
            r = self.distance(i,self.xpos+(self.L)/2+(self.B)/2,self.ypos+(self.B)/2)
        elif(index==2):
            r = self.distance(i,self.xpos+(self.L)/2+(self.B)/2,self.ypos-(self.B)/2)
        return k*(k1+k2*r*r)

    def total_activation(self):
        total=0
        for i in range(m):
            total1+=self.activation(i,1)
            total2+=self.activation(i,2)
        return total1,total2


    def drive(self,xspeed,yspeed):
        for i in range(m):
            x,y =stim[i].location()
            v1 = self.activation(i,1)
            v2 = self.activation(i,2)
            xcoeff,ycoeff = self.sign(i)
            xspeed += xcoeff*(v1+v2)/2
            yspeed += -ycoeff*((v1+v2)**2)/4

        if self.xpos > 2*D:
            self.xpos = 0
        elif self.xpos <= 0:
            self.xpos = 2*D
        if self.ypos >= D:
            self.ypos = 0
        elif self.ypos <= 0:
            self.ypos = D

        self.xpos = self.xpos + xspeed
        self.ypos = self.ypos + yspeed

        return xspeed,yspeed

    def sign(self,i):
        sx,sy = stim[i].location()
        x,y = self.xpos,self.ypos
        xcoeff=0
        ycoeff=0
        if(sx<x):
            xcoeff = -1
        else:
            xcoeff = 1
        if(sy<y):
            ycoeff = 1
        else:
            ycoeff = -1
        return xcoeff,ycoeff

#color,xpos,ypos,L,B,l,b
d=3
c=color(250,0,250)
n=int(random.uniform(1,1000))
objs = list()
for i in range(n):
    objs.append(vehicle(random.uniform(0,2*D), random.uniform(0,D), 8*d, 4*d, 2*d, d))

def setup():
    size(2*D,D)

def draw():
  background(100,100,0)
  for i in range(m):
    stim[i].display()
    stim[i].move()

  for i in range(n):
      objs[i].drive(0,0)
      objs[i].display()
