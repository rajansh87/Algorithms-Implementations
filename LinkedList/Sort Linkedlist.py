class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

arr=[1]
#inserting elements in first list
list1=ListNode(arr[0])
root=list1
for i in arr[1::]:      
    temp=ListNode(i)
    list1.next=temp
    list1=list1.next

    
root2=root
arr=[]
while(root!=None):
    arr.append(root.val)
    root=root.next
root=root2
arr.sort()
list1=ListNode(arr[0])
root=list1
for i in arr[1::]:      
    temp=ListNode(i)
    list1.next=temp
    list1=list1.next
return root

