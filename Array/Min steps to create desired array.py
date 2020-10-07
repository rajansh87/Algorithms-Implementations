arr=[16,16,16]
n=len(arr)
#min steps to get desired array after operations
#Operations are either increase by one or multiply by 2
#so we're doing reverse engineering and converting target
#array to initial array rather than converting initial
#array of all zero's to final target array.

def func1(target,n):
    result=0
    while(target!=[0]*n):
        even=0
        for i in range(n):
            if target[i]%2!=0:
                target[i]-=1
                result+=1
        if target!=[0]*n:
            for i in range(n):
                target[i]/=2
            result+=1
    print(result)
