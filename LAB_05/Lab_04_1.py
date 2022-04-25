
def Hanoi_req(n: int, sour: str, dest:str, buff:str)->None: #2^n-1 dla 3 -> 7; dla 4 ->15 itd
    '''
    hanoi iteration
    '''
    if n==1:
        print('move from:'+str(sour)+' to '+str(dest))
    else:
        Hanoi_req(n-1,sour,buff,dest)
        print('move from:'+str(sour)+' to '+str(dest))
        Hanoi_req(n-1,buff,dest,sour)

def make_hanoi(n:int):
    hanoi=[]
    for i in range(n):
        hanoi.append(n-i)
    return hanoi

def possible_move(a:str,b:str,x:list,y:list)->None:
    if len(y)==0:
        y.append(x[len(x)-1])
        x.remove(x[len(x)-1])
        print('Move disk from '+a+' to '+b)
    elif len(x)==0:
        x.append(y[len(y)-1])
        y.remove(y[len(y)-1])
        print('Move disk from '+b+' to '+a)
    elif x[len(x)-1]<y[len(y)-1]:
        y.append(x[len(x)-1])
        x.remove(x[len(x)-1])
        print('Move disk from '+a+' to '+b)
    else:
        x.append(y[len(y)-1])
        y.remove(y[len(y)-1])
        print('Move disk from '+b+' to '+a)

def Hanoi_2(n:int, sour:str, dest:str, buff:str)->None:
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

Hanoi_req(3,'sour','dest','buff')

Hanoi_2(3,'sour','dest','buff')