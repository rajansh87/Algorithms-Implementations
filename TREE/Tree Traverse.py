class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
def preOrder(root):
    if(root!=None):
        print(root.data,end=" ")
        preOrder(root.left)
        preOrder(root.right)
def postOrder(root):
    if(root!=None):
        postOrder(root.left)
        postOrder(root.right)
        print(root.data,end=" ")
def inOrder(root):
    if(root!=None):
        inOrder(root.left)
        print(root.data,end=" ") 
        inOrder(root.right)
               
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
print("In order Traversal is : ")
inOrder(root)
print("\nPre order Traversal is : ")
preOrder(root)
print("\nPost order Traversal is : ")
postOrder(root)
