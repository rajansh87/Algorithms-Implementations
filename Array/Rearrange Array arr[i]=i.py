arr=[-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
n=len(arr)
#rearrange array such that arr[i]=i

def func1(arr,n):
    for i in range(n):
        if arr[i]!=-1 and arr[i]!=i:
            temp=arr[i]
            while arr[temp]!=-1 and arr[temp]!=temp:
                temp2=arr[temp]
                arr[temp]=temp
                temp=temp2
            arr[temp]=temp
            if arr[i]!=i:
                arr[i]=-1
        
