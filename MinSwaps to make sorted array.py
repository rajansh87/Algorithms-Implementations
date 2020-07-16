def minimumSwaps(arr): 
    a = dict(enumerate(arr,1))
    b = {v:k for k,v in a.items()}
    count = 0
    for i in a:
        x = a[i]
        if x!=i:
            y = b[i]
            a[y] = x
            b[x] = y
            count+=1
    return count
        
n = int(input())
arr = list(map(int,input().split()))

print(minimumSwaps(arr))
