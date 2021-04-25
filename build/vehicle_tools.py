import random
import math
# calculates Euclidean distance between sensor and stimulus
def distance(x,y,sx,sy):
    return sqrt((x-sx)**2+(y-sy)**2)

# i : activation due to i'th stimulus
# index : refers to index of sensor (in case of multiple)
def activation(x,y,sx,sy,type):
    r = distance(x,y,sx,sy)
    if(type == "1b" or type == "3a" or type == "3b"):
        k=.1
        k1=1
        k2=.0001
        return k*(k1+k2*r*r)
    elif(type == "1a" or type == "2a" or type == "2b"):
        k=10000
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
