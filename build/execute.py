import random
import math
import stimulus
import vehicle
# Remember to check on path of the stimulus image file at line 9
# Command for running the simulation: java -jar processing-py.jar execute.py ; remember 'cd build'

D = 600  # window height
d = 2   # vehicle size parameter 
img = loadImage("F:\Linux Backup\Desktop\Work\Active\BV Project\Simulations-of-Braitenberg-Vehicles\stimulus_data\cry.jpg")


flag = input("\n\n\nPress 1 for single fixed stimuli, \nPress 2 for multiple moving stimuli,\nPress 3 for multiple fixed stimuli. \n\n")
if (flag==2 or flag==3):
    num = input("\nMaximum no. of stimulus allowed: ")
elif (flag==1):
    num = 1

m = int(random.uniform(1,num+1))    # number of stimuli in the environment
stim = list()  # creating an array of stimulus


for i in range(m):
    if(flag==1):
        stim.append(stimulus.stimulus(img, 600, 300, 0, 0))
    elif(flag==2):
        stim.append(stimulus.stimulus(img, random.uniform(0,2*D), random.uniform(0,D), random.uniform(0,10), random.uniform(0,10)))
    elif(flag==3):
        stim.append(stimulus.stimulus(img, random.uniform(0,2*D), random.uniform(0,D), 0,0))

n = int(random.uniform(100,500))    # number of vehciles in the environment
objs = list()   # creating an array of vehicles
for i in range(n):
    alpha = 2 * math.pi * random.uniform(0,1)
    objs.append(vehicle.vehicle(random.uniform(0,2*D), random.uniform(0,D), d, stim, alpha))


print "\n\nNo. of stimuli in the environment: ", m
print "No. of vehciles in the environment: ", n

# take vehicle type from terminal
type = input("\nPlease input vehicle type, e.g. 2a, 3b etc.:")

# decide on wiring weights based on vehicle type
if(type == "1a" or type == "1b"):
    w1,w2,w3,w4 = 1,1,1,1
elif(type == "2a" or type == "3a"):
    w1,w2,w3,w4 = 1,1,0,0           # parallel wiring
elif(type == "2b" or type == "3b"):
    w1,w2,w3,w4 = 0,0,1,1           # crossed wiring
else:
    w1,w2,w3,w4 = 0,0,0,0



# setting up the environment window interface
def setup():
    size(2*D,D)
def draw():
  background(100,100,0)     # background of environment
  for i in range(m):
    # processing display and movement of stimulus
    stim[i].display()
    stim[i].move()

  for i in range(n):
    # processing display and movement of stimulus
    objs[i].move(type,w1,w2,w3,w4)   # moves as per "1a" behaviour
    objs[i].display()
