class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
arr=[1,2,3,4,5,6]
k=2
list1=Node(arr[0])
root=list1
for i in arr[1::]:      
    temp=Node(i)
    list1.next=temp
    list1=list1.next
###################
arr=[]
while(root!=None):
    arr.append(root.data)
    root=root.next
brr=[]
for i in range(0,len(arr),k):
    temp=arr[i:i+k]
    temp.reverse()
    brr+=temp

list1=Node(brr[0])
root=list1
for i in brr[1::]:      
    temp=Node(i)
    list1.next=temp
    list1=list1.next
return root
    


