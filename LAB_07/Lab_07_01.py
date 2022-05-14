if __name__ == '__main__':
    new_file=open('C:\\PY prog\\LAB_07\\patterns\\1000_pattern.txt', 'r').readlines()
    
    coordinates=[]

    for x in range(len(new_file)-2):
        for i in range(len(new_file[x])-2):
            if new_file[x][i]==chr(65) and new_file[x][i+1]==chr(66) and new_file[x][i+2]==chr(67):
                if new_file[x+1][i]==chr(66) and new_file[x+2][i]==chr(67):
                    coordinates.append(str(x)+', '+str(i))


    print(coordinates)

