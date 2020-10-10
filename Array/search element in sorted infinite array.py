arr=[1,5,9,10,15,20]
n=len(arr)
num=15 #to be searched 
#find position of element in sorted infinite array

def func1(arr,num):
    low=0
    high=1
    ans=-1
    while high<num:
        if num>arr[high]:
            low=high
            high*=2
        elif num<arr[high]:
            while(low<high):
                mid=low+high
                mid//=2
                if arr[mid]==num:
                    ans=(mid)
                    break
                elif arr[mid]<num:
                    low=mid+1
                else:
                    high=mid-1
        else:
            ans=(high)
            break
        if ans!=-1:
            break
    print(ans)
