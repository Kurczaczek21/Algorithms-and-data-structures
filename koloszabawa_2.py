from math import sqrt
from random import randint
import statistics
from statistics import mode

class RANDOM:
    def __init__(self):
        list=[]
        for i in range(500):
            list.append(randint(0,100))     #od 0 do 100 wlacznie 
        self.list=list
    
    def printer(self):
        return self.list

    def minimal(self):
        minimal=100
        for line in self.list:
            if line<minimal:
                minimal=line
        return minimal

    def maximum(self):
        max=0
        for line in self.list:
            if line > max:
                max=line
        return max

    def moda(self):
        return(mode(self.list))

    def mediana(self):
        self.list.sort()
        return (self.list[149]+self.list[250])/2

    def odchyl(self):
        sum=0
        srednia=0
        for line in self.list:
            srednia+=line
        srednia = srednia/len(self.list)
        for line in self.list:
            sum+=(line-srednia)*(line-srednia)
        return sqrt(sum/len(self.list))


    # def moda2(self):
    #     return max(set(self.list), key=self.list.count)

x=RANDOM()      #jest __init__ wiec nawiasy!
x.printer()     #nawiasy bo funkcja 
print(x.minimal())
print(x.maximum())
print(x.moda())
# print(x.moda2())
print(x.mediana())
print(x.odchyl())

file=open('plik.txt','w')
file.write(' '.join([str(elem) for elem in x.printer()]))
file.write("\n")
file.write(str(x.minimal())+'    '+str(x.maximum())+'     '+str(x.moda())+'    '+str(x.mediana())+' '+str(x.odchyl()))