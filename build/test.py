import random
import math
class Car(object):
# The Constructor is defined with arguments.
    def __init__(self, c, xpos, ypos, xspeed, yspeed, z, alpha):
        self.c = c  # vehicle color
        # intial co-ordinates
        self.xpos = xpos
        self.ypos = ypos
        # initial speed
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.z = z  # vehicle size scale
        self.alpha = alpha  # intial orientation

    def display(self):
        stroke(0)
        stroke(self.c)
        # print("angle = ",self.alpha)
        self.displayBody()
        self.displayW1()
        self.displayW2()
        self.displaySensors()

        # for vehicles to reappear after crossing the window
        if self.xpos > 2*self.z*100 :
            self.xpos = 0
        if self.ypos > self.z*100 :
            self.ypos = 0
       # self.alpha = self.alpha + math.pi/100
       # print(self.alpha*180/math.pi)


        

    def displayBody(self):
        r = math.sqrt(20) * self.z
        angle = math.atan(1.0/2)
        theta = [2 * math.pi - angle, angle , math.pi - angle, math.pi + angle]
        # adding alpha to each theta
        theta = list(map(lambda t : t + self.alpha, theta))

        x1 = self.xpos+ r*math.cos(theta[0])
        y1 = self.ypos+ r*math.sin(theta[0])
        x2 = self.xpos+ r*math.cos(theta[1])
        y2 = self.ypos+ r*math.sin(theta[1])
        x3 = self.xpos+ r*math.cos(theta[2])
        y3 = self.ypos+ r*math.sin(theta[2])
        x4 = self.xpos+ r*math.cos(theta[3])
        y4 = self.ypos+ r*math.sin(theta[3])

        line(x1, y1, x2, y2)
        line(x2, y2, x3, y3)
        line(x3, y3, x4, y4)
        line(x4, y4, x1, y1)




    def displayW1(self):
        r = [math.sqrt(13) * self.z, math.sqrt(18) * self.z, math.sqrt(34) * self.z, math.sqrt(29) * self.z]
        angle = [math.atan(2.0/3), math.atan(1.0), math.atan(3.0/5), math.atan(2.0/5)]
        theta = [math.pi - angle[0], math.pi - angle[1] , math.pi - angle[2], math.pi - angle[3]]
        # adding alpha to each theta
        theta = list(map(lambda t : t + self.alpha, theta))

        x5 = self.xpos+ r[0]*math.cos(theta[0])
        y5 = self.ypos+ r[0]*math.sin(theta[0])
        x6 = self.xpos+ r[1]*math.cos(theta[1])
        y6 = self.ypos+ r[1]*math.sin(theta[1])
        x7 = self.xpos+ r[2]*math.cos(theta[2])
        y7 = self.ypos+ r[2]*math.sin(theta[2])
        x8 = self.xpos+ r[3]*math.cos(theta[3])
        y8 = self.ypos+ r[3]*math.sin(theta[3])

        line(x5, y5, x6, y6)
        line(x6, y6, x7, y7)
        line(x7, y7, x8, y8)
        line(x8, y8, x5, y5)




    def displayW2(self):
        r = [math.sqrt(13) * self.z, math.sqrt(18) * self.z, math.sqrt(34) * self.z, math.sqrt(29) * self.z]
        angle = [math.atan(2.0/3), math.atan(1.0), math.atan(3.0/5), math.atan(2.0/5)]
        theta = [math.pi + angle[0], math.pi + angle[1] , math.pi + angle[2], math.pi + angle[3]]
        # adding alpha to each theta
        theta = list(map(lambda t : t + self.alpha, theta))

        x9 = self.xpos+ r[0]*math.cos(theta[0])
        y9 = self.ypos+ r[0]*math.sin(theta[0])
        x10 = self.xpos+ r[1]*math.cos(theta[1])
        y10 = self.ypos+ r[1]*math.sin(theta[1])
        x11 = self.xpos+ r[2]*math.cos(theta[2])
        y11 = self.ypos+ r[2]*math.sin(theta[2])
        x12 = self.xpos+ r[3]*math.cos(theta[3])
        y12 = self.ypos+ r[3]*math.sin(theta[3])

        line(x9, y9, x10, y10)
        line(x10, y10, x11, y11)
        line(x11, y11, x12, y12)
        line(x12, y12, x9, y9)


    def displaySensors(self):
        r = [math.sqrt(40) * self.z, math.sqrt(40) * self.z, math.sqrt(16+4.0/9) * self.z, math.sqrt(16+4.0/9) * self.z]
        angle = [math.atan(1.0/3), math.atan(1.0/3), math.atan(1.0/6), math.atan(1.0/6)]
        theta = [2 * math.pi - angle[0], angle[1] , angle[2], 2 * math.pi - angle[3]]
        # adding alpha to each theta
        theta = list(map(lambda t : t + self.alpha, theta))

        x13 = self.xpos+ r[0]*math.cos(theta[0])
        y13 = self.ypos+ r[0]*math.sin(theta[0])
        x14 = self.xpos+ r[1]*math.cos(theta[1])
        y14 = self.ypos+ r[1]*math.sin(theta[1])
        x15 = self.xpos+ r[2]*math.cos(theta[2])
        y15 = self.ypos+ r[2]*math.sin(theta[2])
        x16 = self.xpos+ r[3]*math.cos(theta[3])
        y16 = self.ypos+ r[3]*math.sin(theta[3])

    #    line(x13, y13, x14, y14)
        line(x14, y14, x15, y15)
    #    line(x15, y15, x16, y16)
        line(x16, y16, x13, y13)




    def drive(self):
        # for speed
        self.xpos = self.xpos + self.xspeed
        self.ypos = self.ypos + self.yspeed
        # for acceleration
        self.xspeed = self.xspeed + .0005 * self.xspeed
        self.yspeed = self.yspeed + 0.001 * self.yspeed
        
        self.alpha = math.atan(self.yspeed / self.xspeed)
        
            
            

D=500
n=int(random.uniform(1,50)) # n vehicles appear in the environment
objs = list()
for i in range(n):
    z= 5
    alpha = 2 * math.pi * random.uniform(0,1)
   # print(alpha*180/math.pi,i)
    objs.append(Car(color(random.uniform(0,255), random.uniform(0,255), random.uniform(0,255)), random.uniform(0,2*D), random.uniform(0,D), random.uniform(0,3), random.uniform(0,5), z, alpha))

def setup():
    frameRate(50)
    size(2*D,D)

def draw(): 
  background(100,100,0)
  for i in range(n):
      #objs[i].drive()
      objs[i].display()
