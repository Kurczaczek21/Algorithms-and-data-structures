player = 0
p = 0
previous_moves =[]
global possition
possition = [1 , 2 , 3, 4 ,5 ,6 ,7 ,8 ,9]
gamestatus=1
tracker = 0

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
    print("_______________________")

def pusta_plansza():
    plansza_up(0,0)
    plansza_mid(0,0)
    plansza_down(0,0)

def test_ruchu(pole):
    if int(pole) < 1 or int(pole) > 9:
        return "wrong possition"
    else:
        for z in range(len(previous_moves)):
            if previous_moves[z] == pole:
                return "wrong possition"
        previous_moves.append(pole)
        return pole

def game_reset():
    previous_moves.clear()
    global possition
    possition = [1 , 2 , 3, 4 ,5 ,6 ,7 ,8 ,9]
    global gamestatus
    gamestatus=1
    global player
    palyer = 0
    global p
    p=0
    pusta_plansza()

def game_rematch():
    rewanz = input("    DO YOU WANT TO PLAY AGAIN?\n type:  'yes'   or  'no'    \n" )
    if rewanz == "yes":
        game_reset()
    else:
        if rewanz == "no":
            print(" THANK YOU FOR PLAYING   ")
        else:
            game_rematch()


game_reset()

while gamestatus == 1:
    if possition[0]==possition[4]==possition[8]:
        print(" PLAYER  "+ str(p) +"    WINS !!!!!")
        gamestatus=0
    else:
        if possition[2]==possition[4]==possition[6]:
            print(" PLAYER  "+ str(p) +"    WINS !!!!!")
            gamestatus=0
        else:
            for i in range(0, 3):
                if possition[0+3*i]==possition[1+3*i]==possition[2+3*i]:
                    print(" PLAYER  "+ str(p) +"    WINS !!!!!")
                    gamestatus=0
                    break
                else:
                    if possition[0+i]==possition[3+i]==possition[6+i]:
                        print(" PLAYER  "+ str(p) +"    WINS !!!!!")
                        gamestatus=0
                        break
            else:
                move = input("PLAYER    "+ str(player%2 + 1)+ "   MOVE   ")
                while test_ruchu(move) == "wrong possition":
                    move = input("  ILLEGAL MOVE, TRY AGAIN   ")
                else:
                    ruch(int(move))
                    tracker +=1
    if tracker == 9:
        print("   DRAW  ")
        gamestatus = 0

    if gamestatus==0:   
        game_rematch()

        
