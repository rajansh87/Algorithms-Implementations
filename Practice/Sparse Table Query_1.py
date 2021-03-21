# sum of elements in given range
import math
def buildSparseTable(arr,n):
    for i in range(n):
        lookup[i][0]=arr[i]
    j=1
    while (1<<j)<=n:   # j will change in power of 2: 2,4,8,16,..
        i=0
        while (i+(1<<j)-1)<n:
            if lookup[i][j-1]<lookup[i+(1<<(j-1))][j-1]:
                lookup[i][j]=lookup[i][j-1]
            else:
                lookup[i][j]=lookup[i+(1<<(j-1))][j-1]
            i+=1
        j+=1           

def MinElementInRange(L,R):
    j=int(math.log2(R-L+1))
    if lookup[L][j]<=lookup[R-(1<<j)+1][j]:
        return lookup[L][j]
    else:
        return lookup[R-(1<<j)+1][j]

arr=list(map(int,input("enter elements : ").split()))
n=len(arr)

MAX=500
lookup=[[0 for i in range(MAX)]for j in range(MAX)]
buildSparseTable(arr,n)

m=int(input("query size: "))
query=[]
for i in range(m):
    l,r=map(int,input("L,R :").split())
    #query.append([l,r])
    print("min element in the range [",l,",",r,"] : ",MinElementInRange(l,r))


    

