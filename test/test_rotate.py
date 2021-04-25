import math
alpha = math.pi/3
x = 300
y = 300
z = 10

def setup():
    frameRate(100)
    size(600,600)

def draw(): 
    background(100,100,0)

    global x,y,z
    global alpha
    display(alpha)
    point(x, y)
    r = 2 * math.sqrt(5) * z
    alpha = alpha + math.pi/100
def display(alpha):
    displayBody(alpha)
    displayW1(alpha)
    displayW2(alpha)
    displaySensors(alpha)

def displayBody(alpha):
    global x,y,z
    r = math.sqrt(20) * z
    angle = math.atan(1.0/2)
    theta = [2 * math.pi - angle, angle , math.pi - angle, math.pi + angle]
    # adding alpha to each theta
    theta = list(map(lambda x : x + alpha, theta))

    x1 = x + r*math.cos(theta[0])
    y1 = y + r*math.sin(theta[0])
    x2 = x + r*math.cos(theta[1])
    y2 = y + r*math.sin(theta[1])
    x3 = x + r*math.cos(theta[2])
    y3 = y + r*math.sin(theta[2])
    x4 = x + r*math.cos(theta[3])
    y4 = y + r*math.sin(theta[3])

    line(x1, y1, x2, y2)
    line(x2, y2, x3, y3)
    line(x3, y3, x4, y4)
    line(x4, y4, x1, y1)




def displayW1(alpha):
    global x,y,z
    r = [math.sqrt(13) * z, math.sqrt(18) * z, math.sqrt(34) * z, math.sqrt(29) * z]
    angle = [math.atan(2.0/3), math.atan(1.0), math.atan(3.0/5), math.atan(2.0/5)]
    theta = [math.pi - angle[0], math.pi - angle[1] , math.pi - angle[2], math.pi - angle[3]]
    # adding alpha to each theta
    theta = list(map(lambda x : x + alpha, theta))

    x5 = x + r[0]*math.cos(theta[0])
    y5 = y + r[0]*math.sin(theta[0])
    x6 = x + r[1]*math.cos(theta[1])
    y6 = y + r[1]*math.sin(theta[1])
    x7 = x + r[2]*math.cos(theta[2])
    y7 = y + r[2]*math.sin(theta[2])
    x8 = x + r[3]*math.cos(theta[3])
    y8 = y + r[3]*math.sin(theta[3])

    line(x5, y5, x6, y6)
    line(x6, y6, x7, y7)
    line(x7, y7, x8, y8)
    line(x8, y8, x5, y5)




def displayW2(alpha):
    global x,y,z
    r = [math.sqrt(13) * z, math.sqrt(18) * z, math.sqrt(34) * z, math.sqrt(29) * z]
    angle = [math.atan(2.0/3), math.atan(1.0), math.atan(3.0/5), math.atan(2.0/5)]
    theta = [math.pi + angle[0], math.pi + angle[1] , math.pi + angle[2], math.pi + angle[3]]
    # adding alpha to each theta
    theta = list(map(lambda x : x + alpha, theta))

    x9 = x + r[0]*math.cos(theta[0])
    y9 = y + r[0]*math.sin(theta[0])
    x10 = x + r[1]*math.cos(theta[1])
    y10 = y + r[1]*math.sin(theta[1])
    x11 = x + r[2]*math.cos(theta[2])
    y11 = y + r[2]*math.sin(theta[2])
    x12 = x + r[3]*math.cos(theta[3])
    y12 = y + r[3]*math.sin(theta[3])

    line(x9, y9, x10, y10)
    line(x10, y10, x11, y11)
    line(x11, y11, x12, y12)
    line(x12, y12, x9, y9)


def displaySensors(alpha):
    global x,y,z
    r = [math.sqrt(40) * z, math.sqrt(40) * z, math.sqrt(16+4.0/9) * z, math.sqrt(16+4.0/9) * z]
    angle = [math.atan(1.0/3), math.atan(1.0/3), math.atan(1.0/6), math.atan(1.0/6)]
    theta = [2 * math.pi - angle[0], angle[1] , angle[2], 2 * math.pi - angle[3]]
    # adding alpha to each theta
    theta = list(map(lambda x : x + alpha, theta))

    x13 = x + r[0]*math.cos(theta[0])
    y13 = y + r[0]*math.sin(theta[0])
    x14 = x + r[1]*math.cos(theta[1])
    y14 = y + r[1]*math.sin(theta[1])
    x15 = x + r[2]*math.cos(theta[2])
    y15 = y + r[2]*math.sin(theta[2])
    x16 = x + r[3]*math.cos(theta[3])
    y16 = y + r[3]*math.sin(theta[3])

#    line(x13, y13, x14, y14)
    line(x14, y14, x15, y15)
#    line(x15, y15, x16, y16)
    line(x16, y16, x13, y13)
