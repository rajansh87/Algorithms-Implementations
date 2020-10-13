arr=[1, 4, 45, 6, 10, 8]
s=22
n=len(arr)

#triplet withgiven sum

def func1(arr,n,s):
    first,second,third=0,0,0
    ans=[]
    arr.sort()
    for i in range(n-2):
        first=arr[i]
        low=i+1
        high=n-1
        while(low<high):
            val=first+arr[low]+arr[high]
            if val==s:
                ans=[first,arr[low],arr[high]]
                break
            elif val<s:
                low+=1
            else:
                high-=1
        
        if ans!=[]:
            print(ans)
            break

def func2(arr,n,s):
    ans=[]
    for i in range(n-1):
        brr=set()
        cur_sum=s-arr[i]
        for j in range(i+1,n):
            if cur_sum-arr[j] in brr:
                ans=[arr[i],arr[j],cur_sum-arr[j]]
                break
            brr.add(arr[j])
        if ans!=[]:
            print(ans)
            break









