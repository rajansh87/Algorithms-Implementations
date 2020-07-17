#longest subarray with nomore than 2 distinct value differ by no more than 2
arr=[0,1,2,1,2,3]

n=len(arr)

if n<2:
    print(n)
b=1
bl=1
bh=1
for i in range(1,n):
    if arr[i]==arr[i-1]:
        bl+=1
        bh+=1
    elif arr[i]-1==arr[i-1]:
        bl=bh+1
        bh=1
    elif arr[i]+1==arr[i-1]:
        bh=bl+1
        bl=1
    else:
        bl=1
        bh=1
    b=max(b,bl,bh)
print(b)
