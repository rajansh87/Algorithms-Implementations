from collections import defaultdict as df
n=int(input())
d=df(list)
for i in range(n-1):
    a,b=map(int,input().split())
    d[a].append(b)
    d[b].append(a)
visited =[False]*(n+1)
dp=[0]*(n+1)
s=[]
s.append(1)
while(len(s)>0):
    f=s.pop(0)
    for j in d[f]:
        if visited[j]==False:
            visited[j]=True
            s.append(j)
            dp[j]=dp[f]+1
            #print("DP1",dp[j])
#print(dp)
longestDist1=max(dp)
ans=[0]*n
for i in range(1,len(dp)):
    if dp[i]==longestDist1:
        ans[i-1]=1

index=dp.index(max(dp))
s=[]
dp=[0]*(n+1)
s.append(index)
visited=[False]*(n+1)
while len(s)>0:
    f=s.pop(0)
    for j in d[f]:
        if visited[j]==False:
            visited[j]=True
            s.append(j)
            dp[j]=dp[f]+1
            #print("DP2",dp[j])
longestDist2=max(dp)
for i in range(1,len(dp)):
    if dp[i]==longestDist2:
        ans[i-1]=1
#print(longestDist)
#print(dp)
print(*ans,sep=" ")
