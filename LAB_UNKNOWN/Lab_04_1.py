
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

def Hanoi_2(n:int, sour:str, dest:str, buff:str)->None:
    a=make_hanoi(n) #sour
    b=[]            #buff
    c=[]            #dest
    for i in range(1,2**n):
        if i%3 == 1:
            if len(c)==0 and len(a)!=0:
                c.append(a[len(a)-1])
                a.remove(a[len(a)-1])
                print('Move disk from '+sour+' to '+dest)
            elif len(a)==0 and len(c)!=0:
                a.append(c[len(c)-1])
                c.remove(c[len(c)-1])
                print('Move disk from '+dest+' to '+sour)
            elif a[len(a)-1]<c[len(c)-1]:
                c.append(a[len(a)-1])
                a.remove(a[len(a)-1])
                print('Move disk from '+sour+' to '+dest)
            else:
                a.append(c[len(c)-1])
                c.remove(c[len(c)-1])
                print('Move disk from '+dest+' to '+sour)
            if not a and not b:
                    break
                
        if i%3 == 2:
            if len(b)==0 and len(a)!=0:
                b.append(a[len(a)-1])
                a.remove(a[len(a)-1])
                print('Move disk from '+sour+' to '+buff)
            elif len(a)==0 and len(b)!=0:
                a.append(b[len(b)-1])
                b.remove(b[len(b)-1])
                print('Move disk from '+buff+' to '+sour)
            elif a[len(a)-1]<b[len(b)-1]:
                b.append(a[len(a)-1])
                a.remove(a[len(a)-1])
                print('Move disk from '+sour+' to '+buff)
            else:
                a.append(b[len(b)-1])
                b.remove(b[len(b)-1])
                print('Move disk from '+buff+' to '+sour)
            if not a and not b:
                    break
                
        if i%3 == 0:
            if len(b)==0 and len(c)!=0:
                b.append(c[len(c)-1])
                c.remove(c[len(c)-1])
                print('Move disk from '+dest+' to '+buff)
            elif len(c)==0 and len(b)!=0:
                c.append(b[len(b)-1])
                b.remove(b[len(b)-1])
                print('Move disk from '+buff+' to '+dest)
            elif c[len(c)-1]<b[len(b)-1]:
                b.append(c[len(c)-1])
                c.remove(c[len(c)-1])
                print('Move disk from '+dest+' to '+buff)
            else:
                c.append(b[len(b)-1])
                b.remove(b[len(b)-1])
                print('Move disk from '+buff+' to '+dest)
            if not a and not b:
                    break

Hanoi_req(3,'sour','dest','buff')

Hanoi_2(3,'sour','dest','buff')