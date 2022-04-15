#2019 Piotr Śladowski
#Domyślnie w pamięci jest graf z zadania 10b (Zestaw 3)

import math

class Dijkstra:
    numOfVerticles = 0
    Q = [i for i in range(1,8)]
    S = []
    cost = []
    path = []
    choosen = None
    graph =  [[0, 4, math.inf, 1, math.inf, math.inf, 1],
            [4, 0, 3, 2, math.inf, math.inf, math.inf],
            [math.inf, 3, 0, math.inf, math.inf, math.inf, 2],
            [1, 2, math.inf, 0, math.inf, 3, math.inf],
            [math.inf, math.inf, math.inf, math.inf, 0, 1, 2],
            [math.inf, math.inf, math.inf, 3, 1, 0, 4],
            [1, math.inf, 2, math.inf, 2, 4, 0]
            ]


    def __init__(self):
        if (input("Wprowadzić nowy graf? [y/n]: ") == 'y'):
            self.createGraph()
        else:
            self.numOfVerticles = 7
        self.choosen = int(input("Podaj wierzchołek startowy: "))
        self.Q.remove(self.choosen)
        tempCost = []
        tempPath = []
        for i in range(self.numOfVerticles):
            tempCost.append(math.inf)
            tempPath.append(0)
        tempCost[self.choosen-1] = 0
        self.cost.append(tempCost)
        self.path.append(tempPath)
        self.S.append(self.choosen)

    def createGraph(self):
        self.numOfVerticles = int(input("Podaj liczbę wierzchołków: "))
        self.Q = [i for i in range(1,self.numOfVerticles+1)]
        self.graph = [[0 for x in range(self.numOfVerticles)] for y in range(self.numOfVerticles)]
        print("Podaj wagi krawędzi pomiędzy wierzchołkami\nJeżeli nie są połączone wciśnij enter")
        x = 0
        for o in range(self.numOfVerticles):
            for p in range(x, self.numOfVerticles):
                if o != p:
                    inp = input("{0} - {1}: ".format(o+1, p+1))
                    if (inp == ''):
                        self.graph[o][p] = math.inf
                        self.graph[p][o] = math.inf
                    else:
                        self.graph[o][p] = int(inp)
                        self.graph[p][o] = int(inp)
            x += 1
    

    def updateCost(self):
        nextRow = []
        for i in range(1,self.numOfVerticles+1):
            if i not in self.S:
                previousCost = self.cost[-1][i-1]
                currentCost = self.cost[-1][self.choosen-1] + self.graph[i-1][self.S[-1]-1]
                if currentCost < previousCost:
                    nextRow.append(currentCost)
                else:
                    nextRow.append(previousCost)
            else:
                nextRow.append(self.cost[-1][i-1])
        self.cost.append(nextRow)
        self.updateNeighbours()

    def updateNeighbours(self):
        nextRow = []
        for i in range(self.numOfVerticles):
            if self.cost[-1][i] < self.cost[-2][i]:
                nextRow.append(self.S[-1])
            else:
                nextRow.append(self.path[-1][i])
        self.path.append(nextRow)
        self.RogueOne()

    def RogueOne(self):
        min = None
        min = self.cost[-1][self.Q[0]-1]
        nextOne = None
        nextOne = self.Q[0]
        for el in self.Q:
            if self.cost[-1][el-1] < min:
                min = self.cost[-1][el-1]
                nextOne = el
        self.choosen = nextOne
        self.Q.remove(nextOne)
        self.S.append(nextOne)
        if self.Q == []:
            self.printResults()
        else:
            self.updateCost()
            
    def printResults(self):
        print("Tablica kosztów")
        for row in self.cost:
            print(row)
        print("\nTablica poprzedników")
        for row in self.path:
            print(row)
        print("\nZbiór S")
        print(self.S)
        self.again()
    
    def again(self):
        inp = input("Chcesz z innego wierzchołka? [y/n]: ")
        if inp == 'n':
            quit()
        if inp == 'y':
            self.initialize()

    def initialize(self):
        self.S = []
        self.choosen = int(input("Podaj wierzchołek startowy: "))
        self.Q = [i for i in range(1,self.numOfVerticles+1)]
        self.Q.remove(self.choosen)
        self.S.append(self.choosen)
        self.cost = []
        self.path = []
        tempCost = []
        tempPath = []
        for i in range(self.numOfVerticles):
            tempCost.append(math.inf)
            tempPath.append(0)
        tempCost[self.choosen-1] = 0
        self.cost.append(tempCost)
        self.path.append(tempPath)
        self.updateCost()



di = Dijkstra()
di.updateCost()

