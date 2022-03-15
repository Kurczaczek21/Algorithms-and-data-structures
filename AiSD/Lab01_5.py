player = 1
p = 0
global possition
possition = [1 , 2 , 3, 4 ,5 ,6 ,7 ,8 ,9]

def plansza_up(a, r):
    
    for i in range(0, 3):
        if possition[i]==a :
                if r == 1:
                    possition[i]= "X"
                else:
                    possition[i]= "O"
    print("-------------")
    print("| " + str(possition[0]) + " | " + str(possition[1])+" | "+ str(possition[2])+" |")

def plansza_mid(a, r):
    for i in range(3, 6):
        if possition[i]==a :
            if r == 1:
                possition[i]= "X"
            else:
                possition[i]= "O"
    print("-------------")
    print("| " + str(possition[3]) + " | " + str(possition[4])+" | "+ str(possition[5])+" |")
    
def plansza_down(a, r):
    for i in range(6 ,9):
        if possition[i]==a :
            if r == 1:
                possition[i]= "X"
            else:
                possition[i]= "O"

    print("-------------")
    print("| " + str(possition[6]) + " | " + str(possition[7])+" | "+ str(possition[8])+" |")
    print("-------------")

def ruch(x):
    global p
    global player
    if player%2==1:
        p=1         #gracz 1
    else:
        p=2         #gracz 2
    plansza_up(x, p)
    plansza_mid(x, p)
    plansza_down(x, p)
    player += 1
    print("to byl ruch gracza "+ str(p))


move = input("gdzie?   ")

ruch(int(move))

for j in range(1, 9):
    if possition[0]==possition[4]==possition[8]:
        print("gracz "+ str(p) +" wygrywa !!!!!")
    else:
        if possition[2]==possition[4]==possition[6]:
            print("gracz "+ str(p) +" wygrywa !!!!!")
        else:
            for i in range(0, 3):
                if possition[0+3*i]==possition[1+3*i]==possition[2+3*i]:
                    print("gracz "+ str(p) +" wygrywa !!!!!")
                else:
                    if possition[0+i]==possition[3+i]==possition[6+i]:
                        print("gracz "+ str(p) +" wygrywa !!!!!")
                    else:
                        move = input("RUCH GRACZA "+ str(p)+ " GDZIE IDZIESZ?")
                        ruch(int(move))

#commit testing lol