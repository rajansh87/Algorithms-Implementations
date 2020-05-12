n=int(input())


temp=[]
hashtable={}
s=str(n)
for i in range(len(s)):
    for j in range(i,len(s)):
        temp.append(s[i:j+1])
for i in range(len(temp)):
    mx=1
    p=temp[i]
    for j in range(len(p)):
        mx*=int(p[j])
    hashtable[p]=mx
temp2=[]
for key,value in hashtable.items():
    if value not in temp2:
        temp2.append(value)
if(len(temp)==len(temp2)):
    print(1)
else:
    print(0)
