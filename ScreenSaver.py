#Michael Gardiner
#Screen Saver Lab 5
#Due Date: 10-6-15


import turtle
import random
import math

#Create turtle and set the start and end coordinates as well as the color value
def turtleGenerator(xStart,yStart,xEnd,yEnd, red, green, blue):
    bob = turtle.Turtle()
    bob.shape("blank")
    bob.speed(0)
    bob.color(red, green, blue)
    
    bob.up()
    bob.goto(xStart,yStart)
    bob.down()
    bob.goto(xEnd,yEnd)

def dd():
    num=random.randrange(2,5)
    num2=random.randrange(0,2)
    if num2==0:
        num = -1 * num
    return num


def drawlines():
    """draws random lines on the screen that bounce around"""
    w=350
    h=350
    xStart=0
    yStart=0
    xEnd=0
    yEnd=0
    
    finc=dd()
    jinc=dd()
    kinc=dd()
    minc=dd()

    red=random.random()
    green=random.random()
    blue=random.random()
    e1=random.random()
    e2=random.random()
    e3=random.random()

    inc1=(e1-red)/100
    inc2=(e2-green)/100
    inc3=(e3-blue)/100

    a=0
    while(True):
        
        red = red + inc1
        green = green + inc2
        blue = blue + inc3

        a = a + 1
        
        if a >= 100:
            a = 0
            red=e1
            green=e2
            blue=e3
            e1=random.random()
            e2=random.random()
            e3=random.random()
            inc1=(e1-red)/100
            inc2=(e2-green)/100
            inc3=(e3-blue)/100
 

    #Set Barriers for Screensaver to bounce off walls
        xStart = xStart + finc
        if xStart>w:
            finc = finc * -1
        if xStart<-w:
            finc = finc * -1
        yStart = yStart + jinc
        
        if yStart>h:
            jinc = jinc * -1
        if yStart<-h:
            jinc = jinc * -1
        xEnd = xEnd + kinc
        
        if xEnd>w:
            kinc = kinc * -1
        if xEnd<-w:
            kinc = kinc * -1
        yEnd = yEnd + minc
        
        if yEnd>h:
            minc = minc * -1
        if yEnd<-h:
            minc = minc * -1

            
        turtleGenerator(xStart,yStart,xEnd,yEnd, red, green, blue)
    
def main():
    drawlines()

main()
