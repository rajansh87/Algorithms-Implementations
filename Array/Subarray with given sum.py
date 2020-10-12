arr=[1, 4, 20, 3, 10, 5]
n=len(arr)
num=33
#find subarray with given sum

def func1(arr,num,n):
    curr_sum = arr[0] 
    start = 0
    i = 1
    ans=[]
    while i <= n: 
        while curr_sum>num and start< i-1:           
            curr_sum = curr_sum - arr[start] 
            start += 1
            
        if curr_sum ==num:
            ans=[start,i-1]
            break
        if i < n: 
            curr_sum = curr_sum + arr[i] 
        i += 1
    
    if ans==[]:
        print("not found")
    else:
        print(ans)
