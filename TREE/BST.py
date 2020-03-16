class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

def insert(root,newNode):
    if(root==None):
        root=newode
    else:
        if(root.data>newNode.data):
            if(root.left==None):
                root.left=newNode
            else:
                insert(root.left,newNode)
        else:
            if(root.right==None):
                root.right=newNode
            else:
                insert(root.right,newNode)
        
def search(root,key):
    if(root==None or root.data==key):
        return root
    
    if(key>root.data):
        return search(root.right,key)
    return search(root.left,key)
    
    
arr=[50,30,70,20,40,60,80]
root=Node(arr[0])
root2=root
for i in arr[1::]:
    newNode=Node(i)
    insert(root,newNode)
    print("Node ",newNode.data," inserted")
    root=root2
root=root2
print("Enter Node to be Searched : ")
key=int(input())
loc=search(root,key)
if(loc!=None):
    print("Found")
else:
    print("Not Found")
root=root2
    


    

