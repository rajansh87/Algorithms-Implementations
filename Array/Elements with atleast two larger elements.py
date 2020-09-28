arr=[7,-2,3,4,9,-1]
n=len(arr)
#elements in array which have at-lest two greater elements

def func1(arr,n):
    largest=0
    second_largest=0
    if arr[0]>arr[1]:
        largest=arr[0]
        second_largest=arr[1]
    else:
        largest=arr[1]
        second_largest=arr[0]

    for i in range(2,n):
        if arr[i]>largest:
            largest=arr[i]
            print(second_largest,end=" ")
            second_largest=largest
        elif arr[i]>second_largest:
            print(second_largest,end=" ")
            second_largest=arr[i]
            
        else:
            print(arr[i],end=" ")

    
