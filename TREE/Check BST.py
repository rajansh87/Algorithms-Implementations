class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
 
def checkBST(root):
    return(BSTutils(root,-1000000000000000,1000000000000000))

def BSTutils(root,mi,ma):
    if(root==None):
        return True
    if(root.data<mi or root.data>ma):
        return False
    return(BSTutils(root.left,mi,root.data-1) and
           BSTutils(root.right,root.data+1,ma))

root=Node(3)
root.left=Node(5)
root.right=Node(2)
root.left.left=Node(1)
root.left.right=Node(4)
root.right.left=Node(6)

if(checkBST(root)):
    print("YES")
else:
    print("NO")


    


    

