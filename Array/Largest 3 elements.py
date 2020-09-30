arr=[10, 4, 3, 50, 23, 90]
n=len(arr)
#largest three elements in array

def func1(arr,n):
    first,second,third=-1,-1,-1
    for i in range(n):
        if arr[i]>first:
            third=second
            second=first
            first=arr[i]
        elif arr[i]>second:
            third=second
            second=arr[i]
        else:
            third=arr[i]
    print(first,second,third)
        
