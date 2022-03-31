from math import sin, sqrt
import random

def integral_circle(r, accuracy):
    background=r*r*4
    area=3.141592*r*r
    x_list=[]
    y_list=[]
    counter=0
    for i in range(accuracy):
        x_list.append(random.uniform(0,2*r))
        y_list.append(random.uniform(0,2*r))
        if y_list[i]<sqrt(r*r-(x_list[i]-r)*(x_list[i]-r))+r and y_list[i]>-1*(sqrt(r*r-(x_list[i]-r)*(x_list[i]-r)))+r:
            # print(x_list[i],y_list[i])
            counter+=1
        i+=1

    print(background)
    print(area)
    procent= counter/accuracy
    area_1=procent*background
    print(area_1)

integral_circle(4,100000)