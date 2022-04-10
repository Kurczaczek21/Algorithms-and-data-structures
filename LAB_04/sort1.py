
# ZADANIE 1

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
insertionsort(list)
print(list)

# ZADANIE 2

