class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None
    
def Intersection(root1,root2):
    x,y=root1,root2
    while(root1!=None):
        while(root2!=None):
            if(root1.data==root2.data):
                return root1
            root2=root2.next
        root2=y
        root1=root1.next
    return None

root=Node(8)
root.left=Node(4)
root.left.left=Node(1)
root.left.right=Node(6)
root.left.right.left=Node(5)
root.left.left.right=Node(2)
root.left.left.right.right=Node(3)
root.right=Node(9)


v1,v2=1,2
path1=[]
path2=[]
root2=root
root3=root
#for path 1
while(root!=None):
    if(root.data!=v1):
        path1.append(root.data)
        if(root.data>v1):
            root=root.left
        else:
            root=root.right
    else:
        path1.append(root.data)
        break
root=root2
#for path 2
while(root!=None):
    if(root.data!=v2):
        path2.append(root.data)
        if(root.data>v2):
            root=root.left
        else:
            root=root.right
    else:
        path2.append(root.data)
        break
path1.reverse()
path2.reverse()
#inserting elements in first list
list1=ListNode(path1[0])
root1=list1
for i in path1[1::]:      
    temp=ListNode(i)
    list1.next=temp
    list1=list1.next
#inserting elements in second list
list2=ListNode(path2[0])
root2=list2
for i in path2[1::]:      
    temp=ListNode(i)
    list2.next=temp
    list2=list2.next
root=Intersection(root1,root2)
print(root.data)
    


