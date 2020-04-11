class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

root=Node(1)
root.next=Node(2)
root.next.next=Node(3)
root.next.next.next=Node(4)
root.next.next.next.next=Node(5)

def reverse(root):
    if(root==None or root.next==None):
        return root
    head=reverse(root.next)
    root.next.next=root
    root.next=None
    return head


reverse(root)

"""
class Solution:
    def reverseList(self, root):
        if(root==None):
            return
        self.reverseList(root.next)
        return(root.val)
    
"""
    



    

