if __name__ == '__main__':
    new_file=open('LAB_07\\patterns\\5000_pattern.txt', 'r').readlines()   
    # task no 1; primitive algorithm
    coordinates=[]
    steps_left=0
    steps_right=0

    for x in range(len(new_file)-2):
        steps_left+=1
        for i in range(len(new_file[x])-2):
            steps_right+=1
            if new_file[x][i]==chr(65) and new_file[x][i+1]==chr(66) and new_file[x][i+2]==chr(67) and new_file[x+1][i]==chr(66) and new_file[x+2][i]==chr(67):
                coordinates.append(str(x)+', '+str(i))
    print(coordinates)
    print(steps_left+steps_right)

    #task no 2; Karp-Rabin algorithm
    
    coordinates_2=[]
    
    for x in range(len(new_file)-2):
        for i in range(len(new_file[x])-2):
            if (ord(new_file[x][i])+ord(new_file[x][i+1])+ord(new_file[x][i+2])+ord(new_file[x+1][i])+ord(new_file[x+2][i]))==331:
                if new_file[x][i]==chr(65) and new_file[x][i+1]==chr(66) and new_file[x][i+2]==chr(67) and new_file[x+1][i]==chr(66) and new_file[x+2][i]==chr(67):
                    coordinates_2.append(str(x)+', '+str(i))
                
    print(coordinates_2)
            
        
    



