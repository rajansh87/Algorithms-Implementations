arr=[1,5,9,10,15,20]
m=len(arr)
brr=[2,3,8,13]
n=len(brr)

#merge two sorted array in O(1) space

def func1(arr, brr,m,n):
    for i in range(n-1,-1,-1):
        last=arr[m-1]
        j=m-2
        while(j>=0 and arr[j]>brr[i]):
            arr[j+1]=arr[j]
            j-=1
        if j!=m-2or last>brr[i]:
            arr[j+1]=brr[i]
            brr[i]=last
    print(arr+brr)
