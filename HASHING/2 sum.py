arr=[2,7,11,15]
target=9
if len(arr)<2:
    print([])
hashtable={}
temp=[]
for i in range(len(arr)):
    j=target-arr[i]
    if j in hashtable.keys():
        temp=[hashtable[j]+1,i+1]
    
    hashtable[arr[i]]=i
print(temp)
    

