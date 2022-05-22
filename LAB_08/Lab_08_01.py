if __name__=='__main__':
    coordinates=open('C:\PY prog\LAB_08\TSP.txt','r').readlines()

    for i in range(len(coordinates)):    
        coordinates[i]=coordinates[i].split('\t')
        coordinates[i][2].replace('\n','')
        coordinates[i][0]=float(coordinates[i][0])
        coordinates[i][1]=float(coordinates[i][1])
        coordinates[i][2]=float(coordinates[i][2])

    print(coordinates)
