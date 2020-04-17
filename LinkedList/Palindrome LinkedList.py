class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    


stack=[]
root=Node(1)
temp=Node(2)
root.next=temp
temp=Node(3)
root.next.next=temp
root2=root
while(root!=None):
    stack.append(root.data)
    root=root.next
root=root2
z=0
while(root!=None):
    if(root.data!=stack.pop()):
        z=66
        break
    root=root.next
if(z==0):
    print("Yes")
else:
    print("No")
