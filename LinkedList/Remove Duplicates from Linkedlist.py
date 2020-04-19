class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    


arr=[1,1,2,3,3]
#inserting elements in first list
list1=Node(arr[0])
root=list1
for i in arr[1::]:      
    temp=Node(i)
    list1.next=temp
    list1=list1.next
arr=[]
while(root!=None):
    arr.append(root.data)
    root=root.next
arr=list(set(arr))
list1=Node(arr[0])
root=list1
for i in arr[1::]:      
    temp=Node(i)
    list1.next=temp
    list1=list1.next

    
print(arr)
