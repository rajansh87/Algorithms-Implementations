            

arr=[0,1,0,2,1,0,1,3,2,1,2,1]
water=0
lma,rma=0,0
low=0
high=len(arr)-1
while(low<=high):
    if(arr[low]<arr[high]):
        if(arr[low]>lma):
            lma=arr[low]
        else:
            water+=lma-arr[low]
        low+=1
    else:
        if(arr[high]>rma):
            rma=arr[high]
        else:
            water+=rma-arr[high]
        high-=1
print(water)
