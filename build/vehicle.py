import random
import math
import vehicle_tools  as tools
import stimulus

# vy = 0

class vehicle(object):
    def __init__(self, xpos, ypos, z, stim, alpha):
        self.xpos = xpos
        self.ypos = ypos
        self.z = z # vehicle size scale
        self.stim = stim
        self.alpha = alpha # takes care of vehicle orienation

    def display(self):
        # sets up vehicle color intensity as per net velocity
        if(math.isnan(v)):
            c = color(0)
        else:
            c = color(int(255*(1-math.exp(-v))))
        stroke(c)
        # print("angle = ",self.alpha)
        self.displayBody()
        self.displayW1()
        self.displayW2()
        self.displaySensors()


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

    def sensorLocation(self):
        r = [math.sqrt(40) * self.z, math.sqrt(40) * self.z, math.sqrt(16+4.0/9) * self.z, math.sqrt(16+4.0/9) * self.z]
        angle = [math.atan(1.0/3), math.atan(1.0/3), math.atan(1.0/6), math.atan(1.0/6)]
        theta = [2 * math.pi - angle[0], angle[1] , angle[2], 2 * math.pi - angle[3]]
        # adding alpha to each theta
        theta = list(map(lambda t : t + self.alpha, theta))
        x13 = self.xpos+ r[0]*math.cos(theta[0])
        y13 = self.ypos+ r[0]*math.sin(theta[0])
        x14 = self.xpos+ r[1]*math.cos(theta[1])
        y14 = self.ypos+ r[1]*math.sin(theta[1])
        return x13, y13, x14, y14

    def location(self):
        return self.xpos,self.ypos



    def move(self):
        global v
        v, v1, v2, a1, a2 = 0, 0, 0, 0, 0
        # acquiring instantaneous co-ordinates of sensors
        s1x,s1y,s2x,s2y = self.sensorLocation()
        m = len(self.stim)
        # processing each of m stimuli at a time
        for i in range(m):   
            type = self.stim[i].type
            # decide on wiring weights based on vehicle type
            if(type == "1a" or type == "1b"):
                w1,w2,w3,w4 = 1,1,1,1
            elif(type == "2a" or type == "3a"):
                w1,w2,w3,w4 = 1,1,0,0           # parallel wiring
            elif(type == "2b" or type == "3b"):
                w1,w2,w3,w4 = 0,0,1,1           # crossed wiring
            else:
                w1,w2,w3,w4 = 0,0,0,0

            x,y = self.stim[i].location()    # acquiring location of ith stimulus
            a1 += tools.activation(x,y,s1x,s1y,type)  # activation in 1st sensor due to ith stimulus
            a2 += tools.activation(x,y,s2x,s2y,type)  # activation in 2nd sensor due to ith stimulus

            v1 = w1*a1 + w4*a2  # velocity activation in 1st wheel
            v2 = w3*a1 + w2*a2  # velocity activation in 2nd wheel
        
        v = (v1 + v2) / 2 # net velocity of vehicle

        vx = v * math.cos(self.alpha)
        vy = v * math.sin(self.alpha)

        self.alpha += (v1 - v2) * .05

        # updating the new position as vehicle moves
        self.xpos = self.xpos + vx
        self.ypos = self.ypos + vy

        # to make vehciles reappear from other side of environment as they escape
        if self.xpos > .9*width:
            self.alpha += math.pi
        elif self.xpos <= 0:
            self.alpha += math.pi
        if self.ypos >= height:
            self.alpha += math.pi
        elif self.ypos <= 0:
            self.alpha += math.pi

