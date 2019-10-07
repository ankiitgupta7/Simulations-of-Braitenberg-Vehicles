# Braintenberg Vehicles Simulations
## Content
### 1. What this is about?
### 2. What is to be done?
### 3. The Braitenberg Vehicle
### 4. Environment
### 5. Wiring Rules and Activation Function
### 6. Vehicle Kinematics
### 7. Current Developmental Updates
### 8. Setting up and executing Processing.py code
### 9. Future Developments
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
## 6. Vehicle Kinematics
## 7. Current Developmental Updates
## 8. Setting up and executing Processing.py code
## 9. Future Developments
## 10. Inference and Possible Implementations 
## 11. Acknowledgement
## 12. Reference
