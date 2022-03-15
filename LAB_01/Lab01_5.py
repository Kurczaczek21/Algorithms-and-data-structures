player = 0
p = 0
previous_moves =[]
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
    p=player%2 + 1
    plansza_up(x, p)
    plansza_mid(x, p)
    plansza_down(x, p)
    player += 1
    print("to byl ruch gracza "+ str(p))

def pusta_plansza():
    plansza_up(0,0)
    plansza_mid(0,0)
    plansza_down(0,0)


pusta_plansza()

#move = input("gdzie?   ")

#ruch(int(move))

gamestatus=1

while gamestatus == 1:
    if possition[0]==possition[4]==possition[8]:
        print("gracz "+ str(p) +" wygrywa !!!!!")
        gamestatus=0
    else:
        if possition[2]==possition[4]==possition[6]:
            print("gracz "+ str(p) +" wygrywa !!!!!")
            gamestatus=0
        else:
            for i in range(0, 3):
                if possition[0+3*i]==possition[1+3*i]==possition[2+3*i]:
                    print("gracz "+ str(p) +" wygrywa !!!!!")
                    gamestatus=0
                    break
                else:
                    if possition[0+i]==possition[3+i]==possition[6+i]:
                        print("gracz "+ str(p) +" wygrywa !!!!!")
                        gamestatus=0
                        break
            else:
                move = input("RUCH GRACZA "+ str(player%2 + 1)+ ", GDZIE IDZIESZ?")
                previous_moves.append(move)
                for z in range(len(previous_moves)):
                    for q in range(len(previous_moves)):
                        if previous_moves[z] == previous_moves[q] and z != q:
                            previous_moves.remove(move)
                            move = input("TO POLE JEST JUZ ZAJETE, wybierz inne ")
                ruch(int(move))
    if gamestatus==0:   
        rewanz = input("Grasz nexta?\n type: 'yes' or 'no'" )
        if rewanz == "yes":
            possition = [1 , 2 , 3, 4 ,5 ,6 ,7 ,8 ,9]
            gamestatus=1
            player = 0
            p=0
            pusta_plansza()
        else:
            if rewanz == "no":
                print("Thank You for playing")

        
