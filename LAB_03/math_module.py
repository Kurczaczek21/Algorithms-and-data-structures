from math import sqrt

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circuit(self):  
        return 2 * 3.14 * self.radius

class Triangle:
    def __init__(self, a, b, c):
        self.a, self.b, self.c=a, b, c
    def area(self):
        if (self.a+self.b)<=self.c or self.a+self.c <=self.b or self.b+self.c <=self.a:
            return 'CANT BUILD TRIANGLE'
        else:
            p=(self.a+ self.b + self.c)/2
            return sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

    def circuit(self):
        if (self.a+self.b)<=self.c or self.a+self.c <=self.b or self.b+self.c <=self.a:
            return 'CANT BUILD TRIANGLE'
        else:
            return self.a + self.b + self.c

class Square:
    def __init__(self, a):
        self.a= a

    def area(self):
        return self.a*self.a

    def circuit(self):
        return 4*self.a