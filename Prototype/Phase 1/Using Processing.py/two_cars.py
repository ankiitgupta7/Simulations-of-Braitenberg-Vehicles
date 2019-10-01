class Car(object):
# The Constructor is defined with arguments.
    def __init__(self, c, xpos, ypos, xspeed, yspeed, L, B,l,b):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        self.L = L
        self.B = B
        self.l = l
        self.b = b

    def display(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, self.L, self.B);
        rect(self.xpos-(self.L)/2, self.ypos-(self.B)/2-(self.b)/2, self.l, self.b);
        rect(self.xpos-(self.L)/2, self.ypos+(self.B)/2+(self.b)/2, self.l, self.b);
        line(self.xpos+(self.L)/2, self.ypos+(self.B)/6, self.xpos+(self.L)/2+(self.B)/2, self.ypos+(self.B)/2)
        line(self.xpos+(self.L)/2, self.ypos-(self.B)/6, self.xpos+(self.L)/2+(self.B)/2, self.ypos-(self.B)/2)

    def drive(self):
        self.xpos = self.xpos + self.xspeed;
        if self.xpos > width:
            self.xpos = 0

myCar1 = Car(color(255, 0, 0), 0, 100, 4,5, 24, 12, 8, 3)
myCar2 = Car(color(0, 255, 255), 0, 10, 2,5, 24 , 12, 8, 3)

def setup():
    size(1000,500)

def draw(): 
  background(100,100,0)
  myCar1.drive()
  myCar1.display()
  myCar2.drive()
  myCar2.display()
