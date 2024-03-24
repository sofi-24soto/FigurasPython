from turtle import *
import colorsys

bgcolor('black')
tracer(2)
pensize(2)
h=0

for i in range(195):
    color=colorsys.hsv_to_rgb(h,0.9,1)
    h+=0.006
    pencolor(color)
    lt(179)
    backward(i*0.1)
    circle(i*0.3,120)
    rt(14)
    forward(i*0.1)
    circle(i*0.3,120)

done()