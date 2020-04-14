class Node:
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

arr=[8,4,1]
brr=[8,4,1,2]
#inserting elements in first list
list1=Node(arr[0])
root1=list1
for i in arr[1::]:      
    temp=Node(i)
    list1.next=temp
    list1=list1.next
#inserting elements in second list
list2=Node(brr[0])
root2=list2
for i in brr[1::]:      
    temp=Node(i)
    list2.next=temp
    list2=list2.next
#print(Intersection(root1,root2))
root=Intersection(root1,root2)
    
