class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
arr=[5,8,20]
brr=[4,11,15]
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
newlist=[]
while(root1!=None and root2!=None):
    if(root1.data<root2.data):
        newlist.append(root1.data)
        root1=root1.next
    else:
        newlist.append(root2.data)
        root2=root2.next
if(root1==None):
    if(root2==None):
        print(newlist)
    else:
        while(root2!=None):
            newlist.append(root2.data)
            root2=root2.next
elif(root2==None):
    if(root1==None):
        print(newlist)
    else:
        while(root1!=None):
            newlist.append(root1.data)
            root1=root1.next
print(newlist)
            
    




