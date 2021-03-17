# sum of elements in given range

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

    

    
