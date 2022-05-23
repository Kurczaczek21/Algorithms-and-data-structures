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

def search_min_distances(elements:list, core:int):
    min_distance=[1000,0]
    for i in range(len(elements)):
        distance=sqrt(((elements[int((core+i)%len(elements))][1]-elements[int((core+i+1)%len(elements))][1]))**2+(elements[int((core+i)%len(elements))][2]-elements[int((core+i+1)%len(elements))][2])**2)
        if distance<min_distance[0] and i!=core-1:
            min_distance[0]=distance
            min_distance[1]=elements[int((core+i)%len(elements))][0]
    return min_distance
    

def pathfinder_optimize(source:int,coordinates:list):
    
    coordinates.pop(source-1)
    temp=search_min_distances(coordinates,source)
    coordinates.pop(source-1)
    sum_path=temp[0]
    path_id=[temp[1]]
    for i in range(len(coordinates)-1):
        point=search_min_distances(coordinates,temp[1])
        if  coordinates[i][0]==int(point[1]):
            path_id.append(point[1])
            coordinates.pop(int(point[1]-1))
        sum_path+=point[0]
    print(path_id)
    return sum_path


if __name__=='__main__':
    x=pathfinder_optimize(1,open_file())
    print(x)


