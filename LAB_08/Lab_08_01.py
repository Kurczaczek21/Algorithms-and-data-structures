from math import sqrt

def open_file()-> list:
    """opens file with coordinates
    """
    coordinates=open('C:\PY prog\LAB_08\TSP.txt','r').readlines()

    for i in range(len(coordinates)):    
        coordinates[i]=coordinates[i].split('\t')
        coordinates[i][2].replace('\n','')
        coordinates[i][0]=int(coordinates[i][0])
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

def search_min_distances(elements:list, core:int): #core=index+1 ; index=core-1
    temp_id=0
    min_distance=[1000,0]
    for i in range(len(elements)):
        if elements[i][0]!=core:
            for j in range(len(elements)):
               if elements[j][0]==core:
                    temp_id=j    #element tablicy = temp id
            distance=sqrt(((elements[temp_id][1]-elements[i][1]))**2+(elements[temp_id][2]-elements[i][2])**2)
            if distance<min_distance[0]:
                min_distance[0]=distance
                min_distance[1]=elements[i][0]
    return min_distance
    

def pathfinder_optimize(source:int,coordinates:list): #source = index +1 ; index=source-1
    first_city =coordinates[source-1]
    path_id=[source]
    temp=search_min_distances(coordinates,source)
    coordinates.pop(source-1)
    sum_path=temp[0]
    path_id.append(temp[1])
    core=temp[1]
    for k in range(len(coordinates)-1):
        temp=search_min_distances(coordinates,core)
        for i in range(len(coordinates)):    
            if coordinates[i][0]==core:
                coordinates.pop(i)
                break
        sum_path+=temp[0]
        path_id.append(temp[1])
        core=temp[1]
    sum_path+=sqrt((coordinates[0][1]-first_city[1])**2+(coordinates[0][2]-first_city[2])**2)
    path_id.append(first_city[0])
    return sum_path


if __name__=='__main__':
    minimum_path=1000
    city_begin=0
    for i in range(1,101):
        x=pathfinder_optimize(i,open_file())
        if minimum_path>x:
            minimum_path=x
            city_begin=i
    print(pathfinder_naive(1,open_file()))
    print(minimum_path)
    print(city_begin)
    print(pathfinder_optimize(city_begin,open_file()))

