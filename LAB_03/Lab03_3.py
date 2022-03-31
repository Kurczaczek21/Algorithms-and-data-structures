from math import sin, sqrt
import random

def integral_circle(r, accuracy):
    background=r*r*4
    x_list=[]
    y_list=[]
    counter=0
    for i in range(accuracy):
        x_list.append(random.uniform(0,2*r))
        y_list.append(random.uniform(0,2*r))
        if y_list[i]<sqrt(r*r-(x_list[i]-r)*(x_list[i]-r))+r and y_list[i]>-1*(sqrt(r*r-(x_list[i]-r)*(x_list[i]-r)))+r:
            counter+=1
        i+=1
    
    return (counter/accuracy)*background

print(integral_circle(4,100000))

def integral_sin(accuracy):
    x_list=[]
    y_list=[]
    counter=0
    for i in range(accuracy):
        x_list.append(random.uniform(0,2))
        y_list.append(random.uniform(0,1))
        if y_list[i]<sin(x_list[i]):
            counter+=1
        i+=1
    return (counter/accuracy)*2

print(integral_sin(10000))
