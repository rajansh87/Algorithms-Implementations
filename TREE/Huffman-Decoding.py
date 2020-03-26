class Node:
    def __init__(self,data,freq):
        self.left=None
        self.right=None
        self.data=data
        self.freq=freq

root=Node("x",5)
root.left=Node("x",2)
root.right=Node("A",3)
root.left.left=Node("B",1)
root.left.right=Node("C",1)
s="1001011"        #encoded data
ans=""
root2=root
for i in range(len(s)):
    if(s[i]=="1"):
        root=root.right
    elif(s[i]=="0"):
        root=root.left       
    if(root.left==None and root.right==None):
        ans+=root.data
        root=root2
print(ans)        #decoded data
        
    
