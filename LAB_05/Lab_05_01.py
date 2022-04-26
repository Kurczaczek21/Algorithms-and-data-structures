from time import time

req_moves=0
iter_moves=0

def Hanoi_req(n: int, sour: str, dest:str, buff:str)->None:
    '''
    hanoi recursive solve function
    '''
    global req_moves
    if n>0:
        Hanoi_req(n-1,sour,buff,dest)
        req_moves+=1
        print('move from:'+str(sour)+' to '+str(dest))
        Hanoi_req(n-1,buff,dest,sour)

def make_hanoi(n:int):
    '''
    creates reversed n-length list
    '''
    hanoi=[]
    for i in range(n):
        hanoi.append(n-i)
    return hanoi

def list_change(a:str,b:str,x:list,y:list)->None:
    '''
    moves disc to another stake
    '''
    global iter_moves
    y.append(x[len(x)-1])
    x.remove(x[len(x)-1])
    iter_moves+=1
    print('Move disk from '+a+' to '+b)

def possible_move(a:str,b:str,x:list,y:list)->None:
    '''
    checks which move could be made
    '''
    if len(y)==0:
        list_change(a,b,x,y)
    elif len(x)==0:
        list_change(b,a,y,x)
    elif x[len(x)-1]<y[len(y)-1]:
        list_change(a,b,x,y)
    else:
        list_change(b,a,y,x)

def Hanoi_2(n:int, sour:str, dest:str, buff:str)->None:
    '''
    hanoi iteration solve function
    '''
    a=make_hanoi(n) #sour
    b=[]            #buff
    c=[]            #dest
    for i in range(1,2**n):
        if i%3 == 1:
            possible_move(sour,dest,a,c)
            if not a and not b:
                break
                
        if i%3 == 2:
            possible_move(sour,buff,a,b)
            if not a and not b:
                break
                
        if i%3 == 0:
            possible_move(dest,buff,c,b)
            if not a and not b:
                break

if __name__ == '__main__':
    
    total_start=time()
    
    hanoi_req_time=[]
    hanoi_iter_time=[]
    
    for i in range(1,30):
    # Hanoi recursive solve time: 198.02846217155457        for 1<n<30
    # Hanoi iteration solve time:842.4369783401489
    # Total time: 1040.4659361839294

    # Hanoi recursive solve time: 11.116645336151123        for 3<n<25
    # Hanoi iteration solve time:34.16535544395447
    # Total time: 45.29094314575195

        start=time()
        Hanoi_req(i,'sour','dest','buff')
        hanoi_req_time.append(time()-start)
        
        start=time()
        Hanoi_2(i,'sour','dest','buff')
        hanoi_iter_time.append(time()-start)
    
    print('Hanoi recursive solve time: ' + str(sum(hanoi_req_time))+' and moves: '+str(req_moves))
    print('Hanoi iteration solve time:' + str(sum(hanoi_iter_time))+' and moves: '+str(iter_moves))
    print('Total time: '+ str(time()-total_start))
    
    # print(hanoi_iter_time)
    # print(hanoi_req_time)
    # print(len(hanoi_req_time))
    # print(len(hanoi_iter_time))

    # for i in range(len(hanoi_iter_time)):
    #     print('for '+str(hanoi_iter_time[i])+' disks')
    #     i+=1
    #     print('req time = '+str(hanoi_req_time[i]))
    #     print('ite time = '+str(hanoi_iter_time[i]))
