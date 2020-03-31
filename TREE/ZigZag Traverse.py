class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

def Height(root):
    if(root==None):
        return 0
    else:
        leftHeight=Height(root.left)
        rightHeight=Height(root.right)
        if(leftHeight>rightHeight):
            return leftHeight+1
        else:
            return rightHeight+1

def printRightToLeft(root,level):
    if root is None:
        return
    if level is 1:
        print(root.data,end=" ")
    elif level>1:
        printRightToLeft(root.right,level-1)
        printRightToLeft(root.left,level-1)
        
def printLeftToRight(root,level):
    if root is None:
        return
    if level is 1:
        print(root.data,end=" ")
    elif level>1:
        printLeftToRight(root.left,level-1)
        printLeftToRight(root.right,level-1)
        
def ZigZagTaverse(root):
    flag=0
    height=Height(root)
    for i in range(1,height+1):
        if flag==1:
            printRightToLeft(root,i)
            flag=0
        else:
            printLeftToRight(root,i)
            flag=1
               

root=Node(7)
root.left=Node(6)
root.right=Node(5)
root.left.left=Node(4)
root.left.left.left=Node(2)
root.right.left=Node(3)
root.right.left.right=Node(1)
ZigZagTaverse(root)
"""       7
         / \
        6   5
       /   /
      4   3
     /     \
    2       1
"""



