arr=[1, 4, 20, 3, 10, 5]
n=len(arr)

#Max triplet sum in array

def func1(arr,n):
    first,second,third=-99999999,-99999999,-99999999
    for i in range(n):
        if arr[i]>third:
            first=second
            second=third
            third=arr[i]
        elif arr[i]>second:
            first=second
            second=arr[i]
        elif arr[i]>first:
            first=arr[i]
    print(first+second+third)
            
    








