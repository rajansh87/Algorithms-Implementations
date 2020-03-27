class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

def levelOrderTaverse(root):
    if root==None:
        return 
    temp=root
    que=[temp]
    while(len(que)>0):
        print(que[0].data,end=" ")
        temp=que.pop(0)
        if(temp.left != None):
            que.append(temp.left)
        if(temp.right!=None):
            que.append(temp.right)
        
            
#tree construction
root=Node(4)
root.left=Node(2)
root.right=Node(6)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(5)
root.right.right=Node(7)
root.right.right.right=Node(8)
                                                                 """           (4)
                                                                              /   \
                                                                           (2)     (6)
                                                                           /  \    / \
                                                                        (1)   (3)(5)  (7)
                                                                                        \
                                                                                        (8)
                                                                                                                """
#approach 1:
levelOrderTaverse(root)

#approach 2:    
"""def Height(root):
    if(root==None):
        return 0
    else:
        leftHeight=Height(root.left)
        rightHeight=Height(root.right)
        if(leftHeight>rightHeight):
            return leftHeight+1
        else:
            return rightHeight+1   
def levelOrder(root,level):
    if(root==None):
        return root
    if(level==1):
        print(root.data,end=" ")
    elif(level>1):
        levelOrder(root.left,level-1)
        levelOrder(root.right,level-1)

h=Height(root)
for i in range(1,h+1):
    levelOrder(root,i)

 """


