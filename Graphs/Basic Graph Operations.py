#Graph
class graph:
    def __init__(self,gdict=None):
        if gdict==None:
            gdict={}
        self.gdict=gdict
    #if nothing passed as argument means
    #it is empty dictionary
    #i.e None else use the passed dictionary

    def getVertices(self):
        return list(self.gdict.keys())

    def edges(self):
        return self.findedges()

    def findedges(self):
        edgename=[]
        for vertx in self.gdict:
            for nxtvertx in self.gdict[vertx]:
                if {vertx,nxtvertx} not in edgename:
                    edgename.append({vertx,nxtvertx})
        return edgename

    def addVertex(self,vertx):
        if vertx not in self.gdict:
            self.gdict[vertx]=[]

    def AddEdge(self,edge):
        edge=set(edge)
        vertx1,vertx2=tuple(edge)
        if vertx1 in self.gdict:
            self.gdict[vertx1].append(vertx2)
        else:
            self.gdict[vertx1]=[vertx2]
    
    
graph_elements={"a":["b","c"],"b":["a","d"],
                "c":["a","d"],"d":["e"],
                "e":["d"]
                }
#above key of dictionary represents thevertices of graph and
#values of these keys represents there is an edge between the
#key or vertex to other vertex i.e value.
#i.e for node "a", "b" and "c" are the connected nodes.

g=graph(graph_elements)
print("vertices of graph are : ",g.getVertices())
print("edges of graph are : ",g.edges())
g.addVertex(input("enter new vertex : "))
print("vertices of graph are : ",g.getVertices())
g.AddEdge({"a","e"})#new vertices
g.AddEdge({"a","c"})
print("edges of graph are : ",g.edges())
