#Kadane Algorithm for largest sum contiguous subarray


#code to print also the longest sum contiguous subarray
#but this don't satisfies case when all elements are negative
def maxSubArraySum1(arr,n):
    max_so_far=0
    max_ending_here=0

    start=0
    end=0
    s=0

    for i in range(1,n):
        max_ending_here=max_ending_here+arr[i]

        if max_ending_here>max_so_far:
            max_so_far=max_ending_here
            start=s
            end=i

        if max_ending_here<0:
            max_ending_here=0
            s=i+1

    print("starts from : ",start," and ends at :",end)
    return max_so_far

#efficient code deals case when all elements are negative
def maxSubArraySum2(arr,n): 
    max_so_far=arr[0]
    curr_max=arr[0]
    
    for i in range(1,n):
        curr_max=max(arr[i],curr_max+arr[i])
        max_so_far=max(max_so_far,curr_max)
        
    return max_so_far

arr=[-2,-3,4,-1,-2,1,5,-3]
n=len(arr)
print("Max contiguous subarray sum :",maxSubArraySum1(arr,n))
