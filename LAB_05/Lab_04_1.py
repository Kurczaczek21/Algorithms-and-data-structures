from time import time

def Hanoi_req(n: int, sour: str, dest:str, buff:str)->None:
    '''
    hanoi recursive solve function
    '''
    if n>0:
        Hanoi_req(n-1,sour,buff,dest)
        # print('move from:'+str(sour)+' to '+str(dest))
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
    y.append(x[len(x)-1])
    x.remove(x[len(x)-1])
    # print('Move disk from '+a+' to '+b)

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
    # Hanoi recursive solve time: 198.02846217155457        for n=30
    # Hanoi iteration solve time:842.4369783401489
    # Total time: 1040.4659361839294
        start=time()
        Hanoi_req(i,'sour','dest','buff')
        hanoi_req_time.append(time()-start)
        
        start=time()
        Hanoi_2(i,'sour','dest','buff')
        hanoi_iter_time.append(time()-start)
    
    print('Hanoi recursive solve time: ' + str(sum(hanoi_req_time)))
    print('Hanoi iteration solve time:' + str(sum(hanoi_iter_time)))
    print('Total time: '+ str(time()-total_start))