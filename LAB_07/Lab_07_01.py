from time import time

def naive_search(filename):
    new_file=open('LAB_07\\patterns\\'+filename, 'r').readlines()   # task no 1; primitive algorithm
    coordinates=[]
    for x in range(len(new_file)-2):
        for i in range(len(new_file[x])-2):
            if new_file[x][i]==chr(65) and new_file[x][i+1]==chr(66) and new_file[x][i+2]==chr(67) and new_file[x+1][i]==chr(66) and new_file[x+2][i]==chr(67):
                coordinates.append(str(x)+', '+str(i))
    # print(coordinates)
    
def rabin_karp_algorithm(filename):   
    new_file=open('LAB_07\\patterns\\'+filename, 'r').readlines()            #task no 2; Karp-Rabin algorithm
    coordinates=[]
    for x in range(len(new_file)-2):
        for i in range(len(new_file[x])-2):
            if (ord(new_file[x][i])+ord(new_file[x][i+1])+ord(new_file[x][i+2])+ord(new_file[x+1][i])+ord(new_file[x+2][i]))==331:
                if new_file[x][i]==chr(65) and new_file[x][i+1]==chr(66) and new_file[x][i+2]==chr(67) and new_file[x+1][i]==chr(66) and new_file[x+2][i]==chr(67):
                    coordinates.append(str(x)+', '+str(i))
    # print(coordinates)
if __name__ == '__main__':
    
    naive_time=[]
    rabin_time=[]
    
    for i in range(1,6):
        print(str(i)+'000, naive: ')
        start=time()
        naive_search(str(i)+'000_pattern.txt')
        print(time()-start)
        # naive_time.append(time()-start)
        
        start=time()
        print(str(i)+'000, rabin :')
        rabin_karp_algorithm(str(i)+'000_pattern.txt')
        print(time()-start)
        # rabin_time.append(time()-start)
        print('------------------')
    
    start=time()
    print('8000, naive :')
    naive_search('8000_pattern.txt')
    print(time()-start)
    # naive_time.append(time()-start)
    
    start=time()
    print('8000, rabin :')
    rabin_karp_algorithm('8000_pattern.txt')
    print(time()-start)
    # rabin_time.append(time()-start)
    
    # print('Naive searcg time: ' + str(sum(hanoi_req_time))+' and moves: '+str(req_moves))
    # print('Hanoi iteration solve time:' + str(sum(hanoi_iter_time))+' and moves: '+str(iter_moves))
    # print('Total time: '+ str(time()-total_start))
    
    