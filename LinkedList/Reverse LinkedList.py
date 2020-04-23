class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    

def Reverse(root):
    stack=[]
    while(root!=None):
        stack.append(root.data)
        root=root.next
    return stack
    

arr=[1,2,3,4,5]
#inserting elements in first list
list1=Node(arr[0])
root=list1
for i in arr[1::]:      
    temp=Node(i)
    list1.next=temp
    list1=list1.next
stack=Reverse(root)
reversedList=Node(stack.pop())
root=reversedList
while(len(stack)!=0):      
    temp=Node(stack.pop())
    reversedList.next=temp
    reversedList=reversedList.next
# reversed list
while(root!=None):
    print(root.data," -->  ",end=" ")
    root=root.next
    


