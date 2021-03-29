# search elements in given range

arr=list(map(int,input().split()))
m=int(input("query size: "))
query=[]
for i in range(m):
    l,r,x=map(int,input().split())
    query.append([l,r,x])
query.sort(key=lambda x:x[1])
curL,curR=0,0

freq=dict()
for i in range(len(arr)):
    freq[arr[i]]=0

for i in range(len(query)):
    l,r,x=query[i]
    while curL<l: #move to right
        #curS-=arr[curL]
        freq[arr[curL]]-=1
        curL+=1
    while curL>l: #move to left
        #curS+=arr[curL-1]
        freq[arr[curL-1]]+=1
        curL-=1
    while curR<=r: #move to right
        #curS+=arr[curR]
        freq[arr[curR]]+=1
        curR+=1
    while curR>r+1: #move to left
        #curS-=arr[curR-1]
        freq[arr[curR-1]]-=1
        curR-=1
    if x in freq.keys() and freq[x]!=0:
        print(x,"exits in the range [",l,",",r,"]")
    else:
        print(x,"does not exits in the range [",l,",",r,"]")
    
