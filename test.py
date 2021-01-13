#Richa shenoy and Lucia De Tuya 
#1.2.5 project 
#MAD LIBS VALENTINES EDITION 

import random as r
import turtle as trtl 

# this is the code to draw the background of the MADLIBS 


drawer=trtl.Turtle()

def small_rectangle(): 
    drawer.color("black")
    s = 0 
    while s < 4:
        drawer.forward(50) 
        drawer. right(90)
        s = s+1 

def large_rectangle():
    drawer.color("red")
    l = 0 
    while l <4:
        drawer.forward(100)
        drawer.right(90)
        l=l+1 
