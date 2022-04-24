def Hanoi(n, sour, dest, buff): #2^n-1 dla 3 -> 7; dla 4 ->15 itd
    print(sour,buff,dest)
    if n==1:
        sour-=1
        dest+=1
    else:
        Hanoi(n-1,sour,buff,dest)
        sour-=1
        dest+=1
        Hanoi(n-1,buff,dest,sour)

Hanoi(4,4,0,0)

def Hanoi_2(n, sour, dest, buff):
    i=0
    while sour != None or buff !=None:
        if i%3 == 1:
            Possible move disk between sour and dest
            i+=1
        if i%3 == 2:
            Possible move disk between sour and buff
            i+=1
        if i%3 == 0:
            Possible move disk between buff and dest
            i+=1


    # if n%2 ==0:
    #     #AB AC BC
    # else:
    #     #AC AB BC