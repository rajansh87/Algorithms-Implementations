s="(a)"
charac=["+","-","*","/"]
stack=[]

for i in s:
    if i=="(":
        stack.append(False)
    elif i in charac:
        if not stack:
            continue
        stack[-1]=True
        
    elif i==")":
        if stack[-1]:
            stack.pop()
        else:
            print(1)
print(0)        
         
