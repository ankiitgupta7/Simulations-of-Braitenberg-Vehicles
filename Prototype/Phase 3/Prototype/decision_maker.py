# This code mimics behaviour of Braitenberg Vehicles labeled 2a,2b,3a,3b using Turtle.
# The vehicles judges the stimulus based on its color and acts accordingly.
# Also, shape of stimulus determines the Activation Function for sensory excitation.
# The rules of this judgement is as following.
# Shape
# triangular : Activation = k/(k1+k2*r*r)
# square : Activation = k * (k1 + (k2*r*r))
# Color
# black : Cowardness(2a) provoking
# blue : Aggression(2b) provoking
# green : Love/Attraction(3a) provoking
# yellow : Explorer(3b) provoking
# The initial positions and parameter of vehicle and stimulus are prefixed at values
# which result in best behavioural display.
# However, they can randomised in an appropriate range to make it more expressive.
# Multiple vehicles and stimuli can be put together for more complex behaviours
 
import turtle
import math

wn = turtle.Screen()
wn.bgcolor("grey")
wn.title("Braitenberg Vehicles Simulations")

# To determine the sensory activation due to stimulus
# k,k1,k2 being the parameters


def Afunct(s, r):
	if s.shape() == "triangle":
		k1 = 10000000
		k2 = 50000
		k = 2500000000
		return k/(k1+k2*r*r)
	elif s.shape() == "square":
		k1 = 100
		k2 = 5
		k = .000005
		return k*(k1+k2*r*r)

# To calculate the Euclidean distance between two points


def Edist(x1, x2, y1, y2):
	return math.sqrt((x1-x2)**2+(y1-y2)**2)

# To generate specific stimuli at a particular location


def gen_stim(shape, colour, sx, sy):
	stim = turtle.Turtle()
	stim.shape(shape)
	stim.color(colour)
	stim.penup()
	stim.speed(100)
	stim.goto(sx, sy)
	return stim

# To generate the Effector/Motor of the vehicle


def gen_motor(shape, color, x, y):
	m = turtle.Turtle()
	m.shape(shape)
	m.color(color)
	m.penup()
	m.speed(100)
	m.goto(x, y)
	m.pendown()
	return m


# To generate the Sensors of the vehicle
def gen_sensor(shape, color, x, y):
	sr = turtle.Turtle()
	sr.shape(shape)
	sr.color(color)
	sr.penup()
	sr.speed(0)
	sr.goto(x, y)
	return sr

# To generate a vehicle with sensors, effectors and internal wiring
# g: distance between sensors
# l: length of vehicle
# s: stimulus
# vx, vy are initial positions of the vehicle


def gen_vehicle(g, l, s, vx, vy):
	m = gen_motor("circle", "red", vx, vy)  # generated a motor
	# Locating positions of sensors
	srrx = m.xcor()+g/2
	srry = m.ycor()+l
	srlx = m.xcor()-g/2
	srly = m.ycor()+l

	srr = gen_sensor("circle", "purple", srrx, srry)  # generated right seensor
	srl = gen_sensor("circle", "purple", srlx, srly)  # generated left sensor
	# distance between right sensor and stimulus
	dr = Edist(srrx, s.xcor(), srry, s.ycor())
	# distance between left sensor and stimulus
	dl = Edist(srlx, s.xcor(), srly, s.ycor())

	# sar: sensory activation of right sensor
	# sal: sensory activation of left sensor
	sar = Afunct(s, dr)
	sal = Afunct(s, dl)
	# Initialising all the connection weights to Zero
	w = [0]*5
	# To decide on the behavior of vehicle i.e. w[1]=w[2]=1 for parallel and w[3]=w[4]=1 for cross connections.
	if s.color() == ('black', 'black') or ('yellow', 'yellow'):
		w[3] = 1
		w[4] = 1
	elif s.color() == ('blue', 'blue') or ('green', 'green'):
		w[1] = 1
		w[2] = 1
	# Calulating x and y component of velocity due to each sensor
	srr.dx = w[3]*sal*abs(srl.xcor()-s.xcor())/dl + w[2] * \
            sar*abs(srr.xcor()-s.xcor())/dr
	srl.dx = w[1]*sal*abs(srl.xcor()-s.xcor())/dl + w[4] * \
            sar*abs(srr.xcor()-s.xcor())/dr
	srr.dy = w[3]*sal*abs(srl.ycor()-s.ycor())/dl + w[2] * \
            sar*abs(srr.ycor()-s.ycor())/dr
	srl.dy = w[4]*sar*abs(srr.ycor()-s.ycor())/dr + w[1] * \
            sal*abs(srl.ycor()-s.ycor())/dl
	print(w)
	m.dx = (-abs(srr.dx)+abs(srl.dx))
	m.dy = -(srl.dy+srr.dy)
	print("x = ", m.xcor(), " y = ", m.ycor(), "Vx = ", m.dx,
            "Vy = ", m.dy, " vlx = ", srl.dx, " vrx = ", srr.dx, " dl = ", dl, " dr = ", dr)

	while True:
		srrx = m.xcor()+g/2
		srry = m.ycor()+l
		srlx = m.xcor()-g/2
		srly = m.ycor()+l
		dr = Edist(srrx, s.xcor(), srry, s.ycor())
		dl = Edist(srlx, s.xcor(), srly, s.ycor())
		sar = Afunct(s, dr)
		sal = Afunct(s, dl)
		srl.goto(srlx, srly)
		srr.goto(srrx, srry)
		srr.dx = w[3]*sal*abs(srl.xcor()-s.xcor())/dl + w[2] * \
                    sar*abs(srr.xcor()-s.xcor())/dr
		srl.dx = w[1]*sal*abs(srl.xcor()-s.xcor())/dl + w[4] * \
                    sar*abs(srr.xcor()-s.xcor())/dr
		srr.dy = w[3]*sal*abs(srl.ycor()-s.ycor())/dl + w[2] * \
                    sar*abs(srr.ycor()-s.ycor())/dr
		srl.dy = w[1]*sal*abs(srl.ycor()-s.ycor())/dl + w[4] * \
                    sar*abs(srr.ycor()-s.ycor())/dr

		m.dx = (-abs(srr.dx)+abs(srl.dx))
		if m.dy > 0:
			m.dy = (srl.dy+srr.dy)
		else:
			m.dy = -(srl.dy+srr.dy)

		m.sety(m.ycor()-m.dy)
		m.setx(m.xcor()-m.dx)
		print("x = ", m.xcor(), " y = ", m.ycor(), "Vx = ", m.dx,
                    "Vy = ", m.dy, " vlx = ", srl.dx, " vrx = ", srr.dx, " dl = ", dl, " dr = ", dr, " sal = ", sal, " sar = ", sar)


# The type of provoking can be changed by choosing the stimulus parameters as described below.
# triangle, black : Cowardness(2a) provoking
# triangle, blue : Aggression(2b) provoking
# square, green : Love/Attraction(3a) provoking
# square, yellow : Explorer(3b) provoking
# Creating a stimuli that provokes love/attraction
s1 = gen_stim("square", "green", 0, 0)
# To get the behaviour due to stimulus s1
gen_vehicle(60, 15, s1, -250, -300)

wn.mainloop()
