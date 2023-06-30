add_library('controlP5')
import random
import math
import stimulus
import vehicle
# Remember to check on path of the stimulus image file at line 16-18

# Please note that this code requires the library "controlP5", 
# in order to execute it on the command line with "java -jar processing-py.jar run.py",
# please make sure to have the unzipped controlP5 files in the "libraries" folder 
# other than the "processing-py.jar" file in build directory

D = 650 #canvas dimensions


img1 = loadImage("2a.png")
img2 = loadImage("2b.png")
img3 = loadImage("3a.png")



img = img1, img2, img3

start = 0

# setting up the environment window interface
def setup():
    size(2*D,D)


def draw():
    global cp5  
    global start
    global stim
    global objs
    global n
    global d
    global r
    global fov

    if(frameCount == 1):
        background('#004477')
        fill(126)
        rect(.9*width, 550, 80, 20)
        fill(0)
        textSize(16)
        text("     Run", .9*width, 566)      
        cp5 = ControlP5(this)   
        nAgent = cp5.addSlider("Agents")
        nAgent.setPosition(.9*width,400).setSize(80,20).setRange(1, 1000).setValue(400).setNumberOfTickMarks(1000).setSliderMode(Slider.FLEXIBLE)

        
        scale = cp5.addSlider("scale")
        scale.setPosition(.9*width,430).setSize(80,20).setRange(1, 10).setValue(2).setNumberOfTickMarks(10).setSliderMode(Slider.FLEXIBLE)

        fov_dist = cp5.addSlider("r of FoV")
        fov_dist.setPosition(.9*width,460).setSize(80,20).setRange(0, 900).setValue(400).setNumberOfTickMarks(10).setSliderMode(Slider.FLEXIBLE)

        angle =  cp5.addSlider("FoV Angle")
        angle.setPosition(.9*width,490).setSize(80,20).setRange(0, 360).setValue(270).setNumberOfTickMarks(10).setSliderMode(Slider.FLEXIBLE)


        l = "zero", "one", "two", "three", "four", "five", "six", "seven"
        option = "Fixed","Moving"
        cp5.addScrollableList("Opt for Stimuli Motion").setPosition(.9*width, 5).setSize(100, 50).setBarHeight(10).setItemHeight(10).addItems(option)

        cp5.addScrollableList("2a stimulus population").setPosition(.9*width, 100).setSize(100, 80).setBarHeight(10).setItemHeight(10).addItems(l)
        cp5.addScrollableList("2b stimulus population").setPosition(.9*width, 200).setSize(100, 80).setBarHeight(10).setItemHeight(10).addItems(l)
        cp5.addScrollableList("3a stimulus population").setPosition(.9*width, 300).setSize(100, 80).setBarHeight(10).setItemHeight(10).addItems(l)
        cp5.get(ScrollableList, "2a stimulus population").setType(ControlP5.LIST)
        cp5.get(ScrollableList, "2b stimulus population").setType(ControlP5.LIST)
        cp5.get(ScrollableList, "3a stimulus population").setType(ControlP5.LIST)


        cp5.get(ScrollableList, "Opt for Stimuli Motion").setType(ControlP5.LIST)

    if mousePressed and (mouseButton == LEFT ) and mouseX>.9*width and mouseX<(.9*width+80) and mouseY>550 and mouseY<570:
        stim = list()  # creating an array of stimulus
        flag = int(cp5.getController("Opt for Stimuli Motion").getValue())
        n2a = int(cp5.getController("2a stimulus population").getValue())
        n2b = int(cp5.getController("2b stimulus population").getValue())
        n3a = int(cp5.getController("3a stimulus population").getValue())
        n = int(cp5.getController("Agents").getValue())
        d = int(cp5.getController("scale").getValue())  # accessing vehicle scale parameter
        r = int(cp5.getController("r of FoV").getValue())
        fov = int(cp5.getController("FoV Angle").getValue())


        for i in range(n2a):
            if(flag==1):
                stim.append(stimulus.stimulus(img1, '2a', random.uniform(0,.9*width), random.uniform(0,D), random.uniform(0,3), random.uniform(0,3)))
            elif(flag==0):
                stim.append(stimulus.stimulus(img1, '2a', random.uniform(0,.9*width), random.uniform(0,D), 0,0))


        for i in range(n2b):
            if(flag==1):
                stim.append(stimulus.stimulus(img2, '2b', random.uniform(0,.9*width), random.uniform(0,D), random.uniform(0,3), random.uniform(0,3)))
            elif(flag==0):
                stim.append(stimulus.stimulus(img2, '2b', random.uniform(0,.9*width), random.uniform(0,D), 0,0))



        for i in range(n3a):
            if(flag==1):
                stim.append(stimulus.stimulus(img3, '3a', random.uniform(0,.9*width), random.uniform(0,D), random.uniform(0,3), random.uniform(0,3)))
            elif(flag==0):
                stim.append(stimulus.stimulus(img3, '3a', random.uniform(0,.9*width), random.uniform(0,D), 0,0))



        objs = list()   # creating an array of vehicles
        for i in range(n):
            alpha = 2 * math.pi * random.uniform(0,1)
            objs.append(vehicle.vehicle(random.uniform(0,.9*width), random.uniform(0,D), d, stim, alpha))


        
        start = 1


    if(start==1):
        
        background(0,100,100)     # background of environment
        fill(126)
        rect(.9*width, 0, .1*width, height)
        fill(255)
        rect(.9*width, 550, 80, 20)
        fill(0)
        textSize(16)
        text("Run Again", .9*width, 566)
        
        textSize(12)
        text("Stimulus Provocations", .9*width + 2, 590)
        text("2a: Cowardness", .9*width + 5, 605)
        text("2b: Aggression", .9*width + 5, 620)
        text("3a: Love", .9*width + 5, 635)


        for i in range(len(stim)):
            # processing display and movement of stimulus
            stim[i].display()
            stim[i].move()

        for i in range(n):
            # processing display and movement of stimulus
            objs[i].move(r,fov)  
            objs[i].display()
