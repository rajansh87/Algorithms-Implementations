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
root=Node(4)
root.left=Node(2)
root.right=Node(6)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(5)
root.right.right=Node(7)
root.right.right.right=Node(8)
heightOfTree=Height(root)
"""
                 (4)
                /   \
             (2)     (6)
             /  \    / \
          (1)   (3)(5)  (7)
                          \
                           (8)
"""  
print("Height of the Binary tree is : ",heightOfTree)

