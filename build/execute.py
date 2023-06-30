# deprecated - go for run.py

import random
import math
import stimulus
import vehicle
# Remember to check on path of the stimulus image file at line 9
# Command for running the simulation: java -jar processing-py.jar execute.py ; remember 'cd build'

D = 600  # window height
d = 1   # vehicle size parameter 


img1 = loadImage("./images/2a.png")
img2 = loadImage("./images/2b.png")
img3 = loadImage("./images/3a.png")


img = img1, img2, img3

flag = input("\n\n\nPress 1 to generate moving stimuli,\nPress 2 to generate fixed stimuli. \n\n")
num = input("\nMaximum no. of each type of stimulus allowed: ")


m = num   # number of each type of stimuli in the environment
print "number of each type of stimuli in the environment = ",m
stim = list()  # creating an array of stimulus


for i in range(m):
    if(flag==1):
        stim.append(stimulus.stimulus(img1, '2a', random.uniform(0,2*D), random.uniform(0,D), random.uniform(0,3), random.uniform(0,3)))
        stim.append(stimulus.stimulus(img2, '2b', random.uniform(0,2*D), random.uniform(0,D), random.uniform(0,3), random.uniform(0,3)))
        stim.append(stimulus.stimulus(img3, '3a', random.uniform(0,2*D), random.uniform(0,D), random.uniform(0,3), random.uniform(0,3)))
    elif(flag==2):
        stim.append(stimulus.stimulus(img1, '2a', random.uniform(0,2*D), random.uniform(0,D), 0,0))
        stim.append(stimulus.stimulus(img2, '2b', random.uniform(0,2*D), random.uniform(0,D), 0,0))
        stim.append(stimulus.stimulus(img3, '3a', random.uniform(0,2*D), random.uniform(0,D), 0,0))

n = 500    # number of vehciles in the environment
objs = list()   # creating an array of vehicles
for i in range(n):
    alpha = 2 * math.pi * random.uniform(0,1)
    objs.append(vehicle.vehicle(random.uniform(0,2*D), random.uniform(0,D), d, stim, alpha))


print "\n\nNo. of stimuli in the environment: ", 3*m
print "No. of vehciles in the environment: ", n




# setting up the environment window interface
def setup():
    size(2*D,D)
def draw():
    background(100,100,0)     # background of environment
    
    textSize(16)
    text("2a: Cowardness Provoking Stimulus", 10, 30)
    fill(0, 0, 0)
    text("2b: Aggression Provoking Stimulus", 10, 60)
    fill(0, 0, 0)
    text("3a: Love Provoking Stimulus", 10, 90)

    for i in range(3*m):
        # processing display and movement of stimulus
        stim[i].display()
        stim[i].move()

    for i in range(n):
        # processing display and movement of stimulus
        objs[i].move()   # moves as per "1a" behaviour
        objs[i].display()
