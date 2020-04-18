class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    

def deleteDuplicates(self, A):
    current = A
    isDuplicate = False
    A = prev = ListNode(None)
    
    while current != None:
        if current.next != None and current.val == current.next.val:
            isDuplicate = True
        elif isDuplicate:
            isDuplicate = False
        else:
            prev.next = current
            prev = current
        current = current.next
    
    prev.next = current
    
    return A.next

list1=Node(arr[0])
root=list1
for i in arr[1::]:      
    temp=Node(i)
    list1.next=temp
    list1=list1.next

    
print(arr)
