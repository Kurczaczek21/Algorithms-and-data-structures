from random import randint

# ZADANIE 1

def insertionsort(A: list)->list:
    for i in range(len(A)):
        x=A[i]
        j=i-1
        while j>=0 and A[j] > x:
            A[j+1]=A[j]
            j-=1
        A[j+1]=x
    return A

# ZADANIE 2

def mergesort(A: list)->list:
    if len(A)==1 or len(A)==0:
        return A
    else:
        mid = len(A)/2
        left=A[int(mid):]
        right=A[:int(mid)]
        print(left)
        print(right)
        left_list=mergesort(left)
        right_list=mergesort(right)
        sorted_list=merge(left_list, right_list)
        return sorted_list

def merge(left: list,right: list)->list:
    sorted_list=[]
    l=0
    r=0
    while l<len(left) and r<len(right):
        if left[l]<right[r]:
            sorted_list.append(left[l])
            l+=1
        else:
            sorted_list.append(right[r])
            r+=1
    sorted_list+=left[l:]
    sorted_list+=right[r:]
    return sorted_list

list=[]

for i in range(101):
    list.append(randint(1,1000))

x=mergesort(list)
print(x)
