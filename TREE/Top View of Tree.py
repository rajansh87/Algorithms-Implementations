class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
        self.hd=0

def topView(root):
    if(root==None):
        return
    view=[]
    dic={}
    hd=0
    root.hd=hd
    view.append(root)
    while(len(view)):
        root=view[0]
        hd=root.hd
        if(hd not in dic):
            dic[hd]=root.data
        if(root.left):
            root.left.hd=hd-1
            view.append(root.left)
        if(root.right):
            root.right.hd=hd+1
            view.append(root.right)
        view.pop(0)
    for i in sorted(dic):
        print(dic[i],end=" ")
root=Node(4)
root.left=Node(2)
root.right=Node(6)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(5)
root.right.right=Node(7)
root.right.right.right=Node(8)
"""
                 (4)
                /   \
             (2)     (6)
             /  \    / \
          (1)   (3)(5)  (7)
                          \
                           (8)

"""
topView(root)
