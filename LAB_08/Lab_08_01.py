from math import sqrt
from numpy import power

def open_file()-> list:
    """opens file with coordinates
    """
    coordinates=open('E:\PROGRAMMS\Collage-AiSD\LAB_08\TSP.txt','r').readlines()

    for i in range(len(coordinates)):    
        coordinates[i]=coordinates[i].split('\t')
        coordinates[i][2].replace('\n','')
        coordinates[i][0]=float(coordinates[i][0])
        coordinates[i][1]=float(coordinates[i][1])
        coordinates[i][2]=float(coordinates[i][2])

    return coordinates

def pathfinder_naive(source:int,coordinates:list):
    sum_path=0
    cities=[coordinates[source-1][0]]
    for i in range(len(coordinates)):
        sum_path+=sqrt(((coordinates[(source+i)%len(coordinates)][1]-coordinates[(source+i+1)%len(coordinates)][1]))**2+(coordinates[(source+i)%len(coordinates)][2]-coordinates[(source+i+1)%len(coordinates)][2])**2)
        cities.append(coordinates[(source+i)%len(coordinates)][0])
    print(cities)
    return sum_path

def find_closest_val(core:float,elements:list):
    for i in range(len(elements)):
        if elements[i]==min(elements, key=lambda x:abs(x-core)):
            return i
    # return min(elements, key=lambda x:abs(x-core))

def pathfinder_optimize(source:int,coordinates:list):
    sum_path=0
    x_coordinates=[]
    y_coordinates=[]
    for i in range(len(coordinates)):
        if i== source-1:
            x_coordinates.append(1000)
            y_coordinates.append(1000)
        else:    
            x_coordinates.append(coordinates[i][1])
            y_coordinates.append(coordinates[i][2])
    




if __name__=='__main__':
    x=pathfinder_naive(1,open_file())
    print(x)

