
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

Hanoi_req(3,'sour','buff','dest')

# def possible_move(x: str, y:str):


def Hanoi_2(n:int, sour:str, dest:str, buff:str)->None:
    for i in range(1,2**n):
        if i%3 == 1:
            print('Possible move disk between '+sour+' and '+dest)
        if i%3 == 2:
            print('Possible move disk between '+sour+' and '+buff)
        if i%3 == 0:
            print('Possible move disk between '+buff+' and '+dest)

Hanoi_2(3,'sour','buff','dest')

    # if n%2 ==0:
    #     #AB AC BC
    # else:
    #     #AC AB BC