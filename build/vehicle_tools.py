import random
import math
# calculates Euclidean distance between sensor and stimulus
def distance(x,y,sx,sy):
    return sqrt((x-sx)**2+(y-sy)**2)

# calculates the co-ordinates for different vehicle parts
def coordinates(x,y,d,vx):
    l = 2*d     # length of wheel
    b = d       # breadth of wheel
    L = 8*d     # length of vehicle body
    B = 4*d     # breadth of vehicle body
    
    # centre of wheels: (w1x,w1y),(w2x,w2y)
    # centre of vehicle body: (x,y)
    # origin of sensory antenna: (b1x,b1y),(b2x,b2y)
    # sensor co-ordinates: (s1x,s1y),(s2x,s2y)

    if(vx>0):
        w1x = x-(L)/2
        w1y = y-(B)/2-(b)/2
        w2x = x-(L)/2
        w2y = y+(B)/2+(b)/2
        b1x = x+(L)/2
        b1y = y+(B)/6
        b2x = x+(L)/2
        b2y = y-(B)/6
        s1x = x+(L)/2+(B)/2
        s1y = y+(B)/2
        s2x = x+(L)/2+(B)/2
        s2y = y-(B)/2
    else:
        w1x = x+(L)/2
        w1y = y-(B)/2-(b)/2
        w2x = x+(L)/2
        w2y = y+(B)/2+(b)/2
        b1x = x-(L)/2
        b1y = y+(B)/6
        b2x = x-(L)/2
        b2y = y-(B)/6
        s1x = x-(L)/2-(B)/2
        s1y = y+(B)/2
        s2x = x-(L)/2-(B)/2
        s2y = y-(B)/2

    return w1x,w1y,w2x,w2y,b1x,b1y,b2x,b2y,s1x,s1y,s2x,s2y

# i : activation due to i'th stimulus
# index : refers to index of sensor (in case of multiple)
def activation(x,y,sx,sy,type):
    r = distance(x,y,sx,sy)
    if(type == "1b" or type == "3a" or type == "3b"):
        k=.01
        k1=1
        k2=.0001
        return k*(k1+k2*r*r)
    elif(type == "1a" or type == "2a" or type == "2b"):
        k=1000
        k1=1
        k2=1
        return k/(k1+k2*r*r)

# to calibrate the orientation of vehicle
def sign(cx,x):
    xcoeff = 0
    if(x<cx):
        xcoeff = -1
    else:
        xcoeff = 1
    return xcoeff
