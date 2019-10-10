# Braintenberg Vehicles Simulations
## Content
### 1. What this is about?
### 2. What is to be done?
### 3. The Braitenberg Vehicle
### 4. Environment
### 5. Wiring Rules and Activation Function
### 6. Vehicle Kinematics
### 7. Current Developmental Updates
### 8. Future Developments 
### 9. Setting up and executing Processing.py code
### 10. Inference and Possible Implementations 
### 11. Acknowledgement
### 12. Reference

## 1. What this is about?
This is the implementation of my Braitenberg Vehicle Simulation Proposal, submitted for International Neuroinformatics Coordinating Facility ([INCF](https://www.incf.org/)) at Google Summer of Code, 2019. The prototype developed during proposal making period can be seen [here](https://github.com/ankiitgupta7/Simulations-of-Braitenberg-Vehicles/tree/master/Prototype). It was done using [Turtle](https://docs.python.org/3/library/turtle.html). The content of proposal idea can be found [here](https://drive.google.com/open?id=10oOEA-JDcRCXqQFo1aB8Hm-UIsu4KFgi).<br><br>
The present simulation uses [Processing.py](https://py.processing.org/) for UI support. The code written here are based upon ideas described in the book by the neuroscientist [Valentino Braitenberg](https://en.wikipedia.org/wiki/Valentino_Braitenberg) in his classic book "Vehicles: Experiments in Synthetic Psychology" (1984). The book describes how hypothetical analog vehicles (a combination of sensors, actuators and their interconnections), though simple in design, can exhibit behaviors akin to aggression, love, foresight, and optimism. So, we would see these meaningful behaviours emerge from vehicles as they interact with stimuli in the environment through the programmed simulation.

## 2. What would be the final outcome of this project?
The final result would be an intelligent and autonomous system of "vehicles" from which emergent behaviours could be seen as a result of their interaction with the environmental stimuli. Each vehicle would seem intelligent enough to make decisions with respect to the environmental stimuli around.
<br><br>
As we have multiple vehicles(agents) interacting with multiple moving stimulus, the system of vehicles together might be viewed as an intelligent *swarm*. Moreover, each vehicle can also be set as a stimulus which might result in somemore meaningful behaviour as this would be an exact copy of the natural environment containing living and non-living beings together interacting with each other.

## 3. The Braitenberg Vehicle
A Braitenberg vehicle is an agent that can autonomously move around based on its sensor inputs. It has primitive sensors that measure some stimulus at a point, and wheels (each driven by its own motor) that function as actuators or effectors.

![alt text](https://github.com/ankiitgupta7/Simulations-of-Braitenberg-Vehicles/blob/master/Images/vehicle.png)

Depending on how sensors and wheels are connected, the vehicle exhibits different behaviors (which can be goal-oriented). This means that, depending on the sensor-motor wiring, it appears to strive to achieve certain situations and to avoid others, changing course when the situation changes.

## 4. Environment
The environment consist of multiple number of vehicles and different kinds of stimuli. 
<br><br>
The stimuli are scattered throughout the environment which may or may not be moving. Their positions and movements rules are randomly generated values of a given range.
<br><br>
The vehicle’s initial positions are also randomly generated coordinates within the environment window. The movement of the vehicles are governed by the type of stimulus around and their proximity. So, the vehicle movement is completely dependent upon the stimuli around.

![alt text](https://github.com/ankiitgupta7/Simulations-of-Braitenberg-Vehicles/blob/master/Images/Environment.png)

## 5. Wiring Rules and Activation Function
Each type of vehicle is characterized by these two properties being unique to them. By tweaking these properties we get different emergent behaviors and hence different names are assigned to the vehicles. The vehicle movement is particularly inspired by sensory activation received through its sensors and how this activation is transferred to the motor (Internal Wiring). 
<br><br>
I have used the following expression as the sensory activation function, taking a variable “r” as the euclidean distance between sensor and stimulus.
 <br><br>
A1 = k / ( k1 + k2 * r * r ), for non-inhibited activation, and
<br><br> 
A2 = k / ( k1 + k2 * r * r ), for inhibited activation.
<br><br>
Where, k,k1,k2 are calibrated constants.


So, A1 is used in the case of 1A, 2A, 2B, while A2 is used in the case of 1B, 3A, 3B. Note that these are monotonic functions so for developing the next vehicles which have non-monotonic activation, some different activation function has to be used.
 <br><br>
Talking about the internal wiring, these are merely two simple combinations between the pair of sensors and the wheels. I have defined weights for each internal connection between sensor and wheel. So, it’s very evident that for parallel connection, w1, w2, w3, w4 would be 1, 1, 0, 0 respectively. And for crossed connections, the weights corresponding to w1, w2, w3, w4 would be 1, 1, 0, 0. This can be clearly seen in the implemented code.
<br>

![alt text](https://github.com/ankiitgupta7/Simulations-of-Braitenberg-Vehicles/blob/master/Images/parallel.png)
![alt text](https://github.com/ankiitgupta7/Simulations-of-Braitenberg-Vehicles/blob/master/Images/crossed.png)


## 6. Vehicle Kinematics
Digging into the details of vehicle kinematics of Braitenberg Vehicles, we find that the only thing responsible for their movement is the rotation speed of the two wheels and the difference between them.  
<br>
More specifically, the difference in the rotation speed of the wheels is mainly responsible for deflection from its otherwise straight-line trajectory. So, depending upon the activation received at the wheel rotators and their difference, a resultant vehicle movement is rendered.
<br>
![alt text](https://github.com/ankiitgupta7/Simulations-of-Braitenberg-Vehicles/blob/master/Images/kinematics.png)

## 7. Current Developmental Updates
As of now, I have set up the environment as shown above in section 4. Presently, on executing the main code we get to see the behaviors of a selected (opted) type of vehicle visible through their movement in the environment. So, all the vehicles in the environment are of the same type or alternatively we may assume all the stimuli in the environment provoke the same kind of behavior towards them. At present, the stimuli are set as independely moving image snips representing real stimuli moving across the environment.
<br><br>
One of the important outcomes of the development until now is a new perspective to look at a group of Braitenberg Vehicles as some intelligent swarm. The following are the snippets of the simulation execution.
<br>
* Vehicle 2a with moving stimuli <br>
![alt text](https://github.com/ankiitgupta7/Simulations-of-Braitenberg-Vehicles/blob/master/recordings/moving_2a.gif)
* Vehicle 2a with fixed stimuli <br>
![alt text](https://github.com/ankiitgupta7/Simulations-of-Braitenberg-Vehicles/blob/master/recordings/rest_2a.gif)
* Vehicle 2b with moving stimuli <br>
![alt text](https://github.com/ankiitgupta7/Simulations-of-Braitenberg-Vehicles/blob/master/recordings/moving_2b.gif)
* Vehicle 2b with fixed stimuli <br>
![alt text](https://github.com/ankiitgupta7/Simulations-of-Braitenberg-Vehicles/blob/master/recordings/rest_2b.gif)
* Vehicle 3a with moving stimuli <br>
![alt text](https://github.com/ankiitgupta7/Simulations-of-Braitenberg-Vehicles/blob/master/recordings/moving_3a.gif)
* Vehicle 3a with fixed stimuli <br>
![alt text](https://github.com/ankiitgupta7/Simulations-of-Braitenberg-Vehicles/blob/master/recordings/rest_3a.gif)

## 8. Future Developments 
As per the original plan and GSoC proposal, I am going to take the next developmental steps as following.
* Code rest of the vehicles i.e. vehicle 4 onwards.
* Handle the proximity issues between two vehicles to ensure no collision.
* Let the vehicle orient itself in the direction it would be moving. Presently, it’s either left or right.
* Introduce different types of stimuli apart from images e.g. sound, text, etc. and integrate them into the environment in a representable and meaningful form.
* Apply Deep Learning to get meaning out of various stimuli roaming in the environment and influence the behavior of the vehicles present in the environment.
* Analyze the behavior of the resulting mixed types of vehicles in the environment.


## 9. Setting up and executing Processing.py code
The code written here can be directly run on [Processing Software](https://processing.org/download/) installed on your PC. Make sure to opt for the python-mode while the elementary setup.

Alternatively, you make run these codes from terminal too and editing code in your favorite text editor. Follow the instructions on [this](https://py.processing.org/tutorials/command-line/) page.

## 10. Inference and Possible Implementations 
As it’s very evident from the simulation, one of the major takeaways could be using the Braitenberg Vehicles as intelligent swarms. Also, the simulations can be used to predict paths given different kinds of stimuli roaming around the environment.

## 11. Acknowledgement
I thank Dr. Bradly Alicea for mentoring and holding weekly meetings post-GSoC results and guiding me during my proposal making before the results were announced. I also thank Stefan Dvoretskii, Jesse Parent, and Ziyi Gong for our interactions during the weekly calls.
<br><br>
I sincerely thank Google Summer of Code and INCF for opening the topic as a prospective project and reviewing my proposal on it.

## 12. Reference
* [Processing](https://processing.org/), the organization.
* https://en.wikipedia.org/wiki/Braitenberg_vehicle
