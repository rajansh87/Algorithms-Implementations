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

"""
8
1 3
2 3
3 4
4 5
5 6
6 7
6 8
"""
g=Graph()
n=int(input())
for i in range(n-1):
    u,v=map(int,input().split())
    g.addEdge(u,v)

allDist=[]
for i in range(1,n+1):
    print()
    print("Following is DFS from vertex : ",i)
    temp=g.DFS(i)
    print(*temp,sep=" ")
for i in range(1,n+1):
    print()
    print("Following is BFS from vertex : ",i)
    temp=g.BFS(i)
    print(*temp,sep=" ")
##    allDist.append(temp)
##
##mydic=dict()
##for i in allDist:
##    if len(i) not in mydic.keys():
##        mydic[len(i)]=[i[0],i[-1]]
##    else:
##        mydic[len(i)].append(i[0])
##        mydic[len(i)].append(i[-1])
##maxdist=max(list(mydic.keys()))
##
##ans=[0]*n
##for i in range(len(mydic[maxdist])):
##    ans[mydic[maxdist][i]-1]=1
##    print(mydic[maxdist][i])
##print(ans)
    
