# sum of elements in given range
import math
def buildSparseTable(arr,n):
    for i in range(n):
        lookup[i][0]=arr[i]
    j=1
    for j in range(1,k+1):
        for i in range(n-(1<<j)+1):
            lookup[i][j]=lookup[i][j-1]+lookup[i+(1<<(j-1))][j-1]
        
def SumInRange(L,R):
    ans=0
    for j in range(k,-1,-1):
        if L+(1<<j)-1<=R:
            ans+=lookup[L][j]
            L+=1<<j
    return ans

arr=list(map(int,input("enter elements : ").split()))
n=len(arr)

MAX=500 # max value of array
k=16
lookup=[[0 for i in range(k)]for j in range(MAX)]
buildSparseTable(arr,n)


m=int(input("query size: "))
query=[]
for i in range(m):
    l,r=map(int,input("L,R :").split())
    #query.append([l,r])
    print("sum in the range [",l,",",r,"] : ",SumInRange(l,r))


    

