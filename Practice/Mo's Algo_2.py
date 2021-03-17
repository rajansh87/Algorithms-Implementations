# distinct elements in given range

arr=list(map(int,input().split()))
m=int(input("query size: "))
query=[]
for i in range(m):
    l,r=map(int,input().split())
    query.append([l,r])
query.sort(key=lambda x:x[1])
curL,curR,curS=0,0,0
freq=[-1]*(max(arr)+1)
for i in range(len(arr)):
    freq[arr[i]]=0

for i in range(len(query)):
    l,r=query[i]
    while curL<l: #move to right
        #curS-=arr[curL]
        freq[arr[curL]]-=1
        curL+=1
    while curL>l: #move to left
        #curS+=arr[curL-1]
        freq[arr[curL]]+=1
        curL-=1
    while curR<=r: #move to right
        #curS+=arr[curR]
        freq[arr[curR]]+=1
        curR+=1
    while curR>r+1: #move to left
        #curS-=arr[curR-1]
        freq[arr[curR]]-=1
        curR-=1
    print("distinct elements in range",query[i],": ",end="")
    ans=[]
    for i in range(len(freq)):
        c=lambda x:True if (x>0) else False
        if c(freq[i]):
            ans.append(i)
    print(ans)
    

    
