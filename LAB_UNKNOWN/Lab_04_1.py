def Hanoi(n, sour, dest, buff): #2^n-1 dla 3 -> 7; dla 4 ->15 itd
    print(sour,buff,dest)
    if n==1:
        sour-=1
        dest+=1
        return (str(sour)+str(buff)+str(dest))
    Hanoi(n-1,sour,buff,dest)
    sour-=1
    dest+=1
    Hanoi(n-1,buff,dest,sour)

Hanoi(3,3,0,0)



    # if n%2 ==0:
    #     #AB AC BC
    # else:
    #     #AC AB BC