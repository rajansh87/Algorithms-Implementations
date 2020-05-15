arr=[0,0,1,0,2,1]

dic={}
ans=[]
final=[]
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        s=arr[i]+arr[j]
        if s not in dic:
            dic[s]=[i,j]
        else:
            a,b,c,d=dic[s][0],dic[s][1],i,j
            if a<b and c<d:
                if a<c and b!=d and b!=c:
                    ans=[dic[s][0],dic[s][1],i,j]
                    final.append(ans)
    
final.sort()
print(final[0])
        

