# sum of elements in given range

import math
arr=list(map(int,input().split()))
m=int(input("query size: "))
query=[]
for i in range(m):
    l,r=map(int,input().split())
    query.append([l,r])

dic=dict()
n=len(arr)
rootn=math.sqrt(n)
blocksize=n//rootn
blocksize=int(blocksize)
while len(arr)%blocksize!=0:
    arr.append(0)
    

blocks=[]    
n=len(arr)
for i in range(0,n,blocksize):
    blocks.append(sum(arr[i:i+blocksize]))

query.sort(key=lambda x:x[1])
curL,curR,curS=0,0,0
for i in range(len(query)):
    l,r=query[i]
    s=0
    while l<r and l%blocksize!=0 and l!=0:
        s+=arr[l]
        l+=1
    while l+blocksize<=r:
        s+=blocks[l//blocksize]
        l+=blocksize
    while l<=r:
        s+=arr[l]
        l+=1
    print("sum in range ",query[i]," : ",s)
