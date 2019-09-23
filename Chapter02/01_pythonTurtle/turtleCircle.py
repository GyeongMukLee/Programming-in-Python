import turtle
import math

MyTurtle = turtle.Turtle()
MyTurtle.shape('turtle')

r = 100     # 원의 반지름

'''
for i in range(0, 360):
    MyTurtle.goto(r*math.cos(math.pi/180*i)-r, r*math.sin(math.pi/180*i))

for i in range(0, 360):
    MyTurtle.goto(-1*(r*math.cos(math.pi/180*i)-r), r*math.sin(math.pi/180*i))
'''

for i in range(0, 360):
    MyTurtle.goto(r*math.sin(math.pi/180*i), r*math.cos(math.pi/180*i)-r)

for i in range(0, 360):
    MyTurtle.goto(r*math.sin(math.pi/180*i), -1*(r*math.cos(math.pi/180*i)-r))
