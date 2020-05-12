arr=["cat","dog","god","tca"]

dic={}

count=[0]*27
ind=[]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        count[ord(arr[i][j])-97]+=1
    #dic[i+1]=count
    if tuple(count) not in dic:
        dic[tuple(count)]=[i+1]
    else:
        dic[tuple(count)].append(i+1)
    count=[0]*27
        

brr=list(dic.values())
print(brr)
