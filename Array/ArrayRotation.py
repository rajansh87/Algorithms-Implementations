arr=[1,2,3,4,5,6,7]
n=len(arr)
loc=2

def func1(arr,loc):
    loc-=1 #index starts with 0
    
    for i in range(n-loc-1):
        arr[i],arr[loc+i+1]=arr[loc+i+1],arr[i]
    
    
    if len(arr)%2!=0:
        arr[n-2],arr[n-1]=arr[n-1],arr[n-2]
        
    print(arr)


#Reversal Algo for array rotation
def func2(arr,loc):
    a=arr[:loc]
    b=arr[loc:]
    a=a[::-1]
    b=b[::-1]
    arr=a+b
    arr=arr[::-1]
    print(arr)
