class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

arr=[1]
#inserting elements in first list
k=1
list1=Node(arr[0])
root=list1
for i in arr[1::]:      
    temp=Node(i)
    list1.next=temp
    list1=list1.next
root2=root
n=len(arr)-k
i=0
while(i<n):
    print(root.data)
    root=root.next
    i+=1
#print(root.data)
while(i<len(arr)-1):
    root.data=root.next.data
    i+=1
root=None
root=root2
print(root.data)
