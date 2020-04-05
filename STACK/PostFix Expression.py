s="512+4*+3-"
stack=list(s)
for i in range(len(s)):
    if(s[i]=="+" or s[i]=="-" or s[i]=="*" or s[i]=="/"):
        first=stack.pop()
        second=stack.pop()
        if(s[i]=="+"):
            stack.append(int(second)+int(first))
        elif(s[i]=="-"):
            stack.append(int(second)-int(first))
        elif(s[i]=="*"):
            stack.append(int(second)*int(first))
        elif(s[i]=="/"):
            stack.append(int(second)/int(first))
    else:
        stack.append(s[i])
print(stack.pop())
