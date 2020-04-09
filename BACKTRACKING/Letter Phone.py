s="23"
dic={"0":"0","1":"1","2":"abc","3":"def","4":"ghi","5":"jkl",
     "6":"mno","7":"pqrs","8":"tuv","9":"wxyz","*":"+","#":"#"}
def fun1(s):
    n=len(s)
    ans=[]
    if not s:
        return []
    fun2(ans,s,"",0)
    return ans
def fun2(ans,s,cur,start):
    if start==len(s):
        ans.append(cur)
        return
    else:
        for i in dic[s[start]]:
            fun2(ans,s,cur+i,start+1)


print(fun1(s))

"""
dic={"0":"0","1":"1","2":"abc","3":"def","4":"ghi","5":"jkl",
     "6":"mno","7":"pqrs","8":"tuv","9":"wxyz","*":"+","#":"#"}
s="23"
arr=[]
for i in s:
    arr.append(dic[i])
ans=[]
for i in range(len(s)):
    if not ans:
        ans=dic[s[i]]
    else:
        cur=[]
        for j in ans:
            for k in dic[s[i]]:
                cur.append(j+k)
        ans=cur
print(ans)
"""
