from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def DFSUtil(self, v, visited,visit):
        visited.add(v)
        visit.append(v)#print(v,end=" ")
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited,visit)
        return visit
    def DFS(self, v):
        visited = set()
        visit=[]
        visit=self.DFSUtil(v, visited,visit)
        return visit
    def BFS(self, s):
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(s)
        visited[s] = True
        visit=[]
        while queue:
            s = queue.pop(0)
            visit.append(s)#print (s, end = " ")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        return visit

g=Graph()
n=int(input())
#brr=[-1]*n
color=dict()
color[0]=[]
color[1]=[]
arr=list(map(int,input().split()))
for i in range(n):
    if arr[i]==0:
        color[0].append(i+1)
    else:
        color[1].append(i+1)
for i in range(n-1):
    u,v=map(int,input().split())
    g.addEdge(u,v)
    #brr.insert(u-1,arr[u-1])
    #brr.insert(v-1,arr[v-1])
    #print("a: ",brr)
#crr=[]
#for i in brr:
    #if i!=-1:
        #crr.append(i)
dfs_path=dict()
for i in range(1,n+1):
    temp=g.DFS(i)
    dfs_path[i]=temp

for i in range(n):
    dfs_path[i+1].remove(i+1)
c=0
for i in dfs_path.values():
    for j in color[1]:
        if j in i:
            c+=1
            break
print(c)


    
    

