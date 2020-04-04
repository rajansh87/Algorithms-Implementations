arr=list(map(int,input().split()))
g=[-1]*len(arr)
temp=-1
stack=[]
for i in range(len(arr)):
    while(len(stack)!=0 and stack[len(stack)-1]>=arr[i]):
        stack.pop()
    if(len(stack)!=0):
        g[i]=(stack[len(stack)-1])
    stack.append(arr[i])
print(g)
    
