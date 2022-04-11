from random import randint
from time import time

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

def mergesort2(A: list)->list:
    if len(A)==1 or len(A)==0:
        return A
    else:
        mid = len(A)/2
        left=A[:int(mid)]
        right=A[int(mid):]
        left_list=mergesort2(left)
        right_list=mergesort2(right)
        sorted_list=merge2(left_list, right_list)
        return sorted_list

def merge2(left: list,right: list)->list:
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

def mergesort(A: list,a: int,b: int)->None:
    if a < b:
        c = (a+b)//2
        mergesort(A ,a ,c )
        mergesort(A ,c+1 ,b )
        merge(A, a, c, b)
    
def merge(A: list,start: int ,mid: int, end: int)->None:
    sorted_list=[]
    left=start
    right=mid+1
    while left<mid and right<end:
        if A[left]<A[right]:
            sorted_list.append(A[left])
            left+=1
        else:
            sorted_list.append(A[right])
            right+=1

    while left<=mid:
        sorted_list.append(A[left])
        left+=1
    while right <=end:
        sorted_list.append(A[right])
        right+=1
    
    for i in range(start,end+1):
        A[i]=sorted_list[i-start]

if __name__ == '__main__':
    
    total_start=time()
    
    insort_time=[]
    mersort_time=[]
    pysort_time=[]
    
    for i in range(100):
        random_list_1=[]
        for i in range(10000):
            random_list_1.append(randint(1,1000))
        random_list_2=random_list_1
        random_list_3=random_list_1
        
        start=time()
        insertionsort(random_list_1)
        insort_time.append(time()-start)
        
        start=time()
        mergesort(random_list_2 ,0 ,len(random_list_2)-1)
        mersort_time.append(time()-start)
        
        start=time()
        random_list_3.sort()
        pysort_time.append(time()-start)
    
    print('insert time:' + str(sum(insort_time)))
    print('merge time:' + str(sum(mersort_time)))
    print('python sort time: '+ str(sum(pysort_time)))
    print('Total time: '+ str(time()-total_start))