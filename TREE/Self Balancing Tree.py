class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
        self.height=1

def leftRotate(z):
    y=z.right
    t2=y.left
    #rotste
    y.left=z
    z.right=t2
    #update height
    z.height=1+max(getHeight(z.left),
                      getHeight(z.right))
    y.height=1+max(getHeight(y.left),
                      getHeight(y.right))
    return y

def rightRotate(z):
    y=z.left
    t3=y.right
    #rotste
    y.right=z
    z.left=t3
    #update height
    z.height=1+max(getHeight(z.left),
                      getHeight(z.right))
    y.height=1+max(getHeight(y.left),
                      getHeight(y.right))
    return y
    

def getHeight(root):
    if(root==None):
        return 0
    return root.height

def getBalance(root):
    if(root==None):
        return 0
    return getHeight(root.left)-getHeight(root.right)

def inOrder(root):
    if(root!=None):
        inOrder(root.left)
        print(root.data,end=" ") 
        inOrder(root.right)

def insert(root,data):  #AVL insertion
    if(root==None):
        return Node(data)
    elif(data<root.data):
        root.left=insert(root.left,data)
    else:
        root.right=insert(root.right,data)
        
    root.height=1+max(getHeight(root.left),
                      getHeight(root.right))
    
    balance=getBalance(root)       #Balance Factor
    if(balance>1 and data<root.left.data):   #Rule 1
        return rightRotate(root)
    if(balance<-1 and data>root.right.data):  #Rule 2
        return leftRotate(root)
    if(balance>1 and data>root.left.data):   #Rule 3
        root.left=leftRotate(root.left)
        return rightRotate(root)
    if(balance<-1 and data<root.right.data):   #Rule 4
        root.right=rightRotate(root.right)
        return leftRotate(root)
    
    return root



root=None
root=insert(root,10)
root=insert(root,20)
root=insert(root,30)
root=insert(root,40)
root=insert(root,50)
root=insert(root,25)
inOrder(root)








