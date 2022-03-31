from math import sin, sqrt
import random

def integral_circle(r, accuracy):
    background=r*r*4
    counter=0
    for i in range(accuracy):
        x=random.uniform(0,2*r)
        y=random.uniform(0,2*r)
        if y<=sqrt(r*r-(x-r)*(x-r))+r and y>=-1*(sqrt(r*r-(x-r)*(x-r)))+r:
            counter+=1
    return (counter/accuracy)*background

def integral_sin(accuracy):
    counter=0
    for i in range(accuracy):
        x=random.uniform(0,2)
        y=random.uniform(0,1)
        if y<=sin(x):
            counter+=1
    return (counter/accuracy)*2

print(integral_circle(4,10000000))
print(integral_sin(1000000))
