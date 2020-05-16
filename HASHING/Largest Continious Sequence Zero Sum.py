arr=[1,2,-2,4,-4]

s=0
dic={}
dic[0]=-1
st=-1
en=-1
ma=-9999999999999
ans=[]
for i in range(len(arr)):
    s+=arr[i]
    if s in dic:
        if ma<i-dic[s]:
            st=dic[s]+1
            en=i
            ma=i-dic[s]
    else:
        dic[s]=i
if st>=0 and en>=0:
    for i in range(st,en+1):
        ans.append(arr[i])
print(ans)
        


