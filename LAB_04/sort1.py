
# ZADANIE 1

from re import A


def insertionsort(A):
    for i in range(len(A)):
        x=A[i]
        j=i-1
        while j>=0 and A[j] > x:
            A[j+1]=A[j]
            j-=1
        A[j+1]=x
    return A

list=[5,3,1,24,54,3,54,2,3,87,43]
print(list)
# insertionsort(list)
print(list)

# ZADANIE 2

def mergesort(A, a, b):
    if a<b:
        c=(a+b)/2
        mergesort(A, a, c)
        mergesort(A, c+1, b)
        merge(T, a, c , b)
    return A

mergesort(A)