import random
import math
import vehicle_tools  as tools

# vy = 0

class vehicle(object):
    def __init__(self, x, y, d, stim):
        self.x = x
        self.y = y
        self.d = d
        self.stim = stim

    def display(self):

        # acquiring instantaneous co-ordinates of vehcile position
        w1x,w1y,w2x,w2y,b1x,b1y,b2x,b2y,s1x,s1y,s2x,s2y = tools.coordinates(self.x,self.y,self.d, vx)

        # setting up the vehcile dimensions
        l = 2*self.d
        b = self.d
        L = 8*self.d
        B = 4*self.d
        # calculates net velocity of vehicle
        v = sqrt(vx**2+vy**2)
        # sets up vehicle color intensity as per net velocity
        c = color(int(255*(1-math.exp(-v))))
        fill(c)
        # draw the vehicle based on instantaneous co-ordinates
        rectMode(CENTER)
        rect(self.x, self.y, L, B);
        rect(w1x, w1y, l, b)
        rect(w2x, w2y, l, b)
        line(b1x, b1y, s1x, s1y)
        line(b2x, b2y, s2x, s2y)


    def location(self):
        return self.x,self.y



    def move(self, type, w1, w2, w3, w4):

        global vx,vy
        vx = 0
        vy = 0
        # acquiring instantaneous co-ordinates of vehcile position
        w1x,w1y,w2x,w2y,b1x,b1y,b2x,b2y,s1x,s1y,s2x,s2y = tools.coordinates(self.x,self.y,self.d,vx)


        m = len(self.stim)
        # processing each of m stimuli at a time
        for i in range(m):
            x,y = self.stim[i].location()    # acquiring location of ith stimulus
            a1 = tools.activation(x,y,s1x,s1y,type)  # activation in 1st sensor due to ith stimulus
            a2 = tools.activation(x,y,s2x,s2y,type)  # activation in 2nd sensor due to ith stimulus
            v1 = w1*a1 + w4*a2  # velocity activation in 1st wheel
            v2 = w3*a1 + w2*a2  # velocity activation in 2nd wheel
            # to decide orientation of vehicle wrt. stimuli
            xcoeff = tools.sign(self.x,x)
            # net horizontal velocity due to all m stimulus
            vx += xcoeff*(v1+v2)/2
            # net vertical velocity due to all m stimulus
            # note that it is acceleration
            vy += (v2-v1)*((v1+v2)**2)/(.04*v1)
        # to make vehciles reappear from other side of environment as they escape
        if self.x > width:
            self.x = 0
        elif self.x <= 0:
            self.x = width
        if self.y >= height:
            self.y = 0
        elif self.y <= 0:
            self.y = height

        # updating the new position as vehicle moves
        self.x = self.x + vx
        self.y = self.y + vy
