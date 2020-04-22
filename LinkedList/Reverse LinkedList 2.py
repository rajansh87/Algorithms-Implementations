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
m=2
n=4
#inserting elements in first list
list1=Node(arr[0])
root=list1
for i in arr[1::]:      
    temp=Node(i)
    list1.next=temp
    list1=list1.next
arr=[]
root2=root
while(root!=None):
    arr.append(root.data)
    root=root.next
arr1=arr[0:m-1]
arr2=arr[n::]
#print(arr1)
#print(arr2)

root=root2
list1=Node(arr[m-1])
root=list1
for i in arr[m:n]:      
    temp=Node(i)
    list1.next=temp
    list1=list1.next
root2=root
stack=Reverse(root)
reversedList=Node(stack.pop())
root=reversedList
while(len(stack)!=0):      
    temp=Node(stack.pop())
    reversedList.next=temp
    reversedList=reversedList.next
# reversed list
mylist=arr1
while(root!=None):
    mylist.append(root.data)
    root=root.next
mylist+=arr2
root=root2

list1=Node(mylist[0])
root=list1
for i in mylist[1::]:      
    temp=Node(i)
    list1.next=temp
    list1=list1.next

return root

