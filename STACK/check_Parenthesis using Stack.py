s=")}}}(}]}(}}(}[]])](}"
stack=[]
for i in s:
    if i=="[" or i=="(" or i=="{":
        stack.append(i)
    elif i=="]":
        if len(stack)!=0:
            if stack[-1]=="[":
                stack.pop()
            else:
                print(0)
        else:
            print(0)
    elif i==")":
        if len(stack)!=0:
            if stack[-1]=="(":
                stack.pop()
            else:
                print(0)
        else:
            print(0)
    elif i=="}":
        if len(stack)!=0:
            if stack[-1]=="{":
                stack.pop()
            else:
                print(0)
        else:
            print(0)
        
if(len(stack)==0):
    print(1)
else:
    print(0)
