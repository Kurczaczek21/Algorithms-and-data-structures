from math import sin, sqrt
from random import randint

def integral_circle(r, accuracy):
    background=r*r*4
    area=3.14*r*r
    x_list=[]
    y_list=[]
    for i in range(accuracy):
        x_list.append(randint(0,r))
        y_list.append(randint(0,r))
        if y_list[i]<sqrt(r*r-(x_list[i]-r)*(x_list[i]-r))+r or y_list[i]>sqrt(r*r-(x_list[i]-r)*(x_list[i]-r))+r:
            print("pepaTAS")

        i+=1

    print(background)
    print(area)
    print(x_list)
    print(y_list)

integral_circle(4,100)