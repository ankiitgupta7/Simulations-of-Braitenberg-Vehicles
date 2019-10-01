import turtle
import math

wn = turtle.Screen()
wn.bgcolor("grey")
wn.title("Vehicle One: Getting Around (Negatively Tuned)")

source = turtle.Turtle()
source.shape("circle")
source.color("black")
source.penup()
source.speed(0)
source.goto(0,0)

v = turtle.Turtle()
v.shape("circle")
v.color("red")
v.penup()
v.speed(0)
x= -520
y = -300
k1 = 1000
k2 = .05
k = .0005
v.goto(x,y)

d = math.sqrt((v.xcor()-source.xcor()) ** 2 +
              (v.ycor()-source.ycor()) ** 2)
vel = k * (k1 + (k2*d ** 2))
v.dx = vel*(v.xcor()-source.xcor())/d
v.dy = vel*(v.ycor()-source.ycor())/d

v.pendown()
while True:
    d = math.sqrt((v.xcor()-source.xcor()) ** 2 +
                  (v.ycor()-source.ycor()) ** 2)
    vel = k * (k1 +(k2*d ** 2))
    if v.dx < 0 :
        v.dx =- vel*abs(v.xcor()-source.xcor())/d
    else:
        v.dx = vel*abs(source.xcor()-v.xcor())/d
    if v.dy < 0 :
        v.dy =- vel*abs(v.ycor()-source.ycor())/d
    else:
        v.dy = vel*abs(source.ycor()-v.ycor())/d
    v.sety(v.ycor()-v.dy)
    v.setx(v.xcor()-v.dx)
    print("x = ", v.xcor(), " y = ", v.ycor(), " d = ",
          d, "Vx = ", v.dx, "Vy = ", v.dy, " vel = ", vel)



wn.mainloop()
