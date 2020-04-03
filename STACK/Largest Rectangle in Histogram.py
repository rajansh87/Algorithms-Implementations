arr=[2,1,5,6,2,3]
n = len(arr)
i = 0
curr = 0
largest_area = 0
stack = []
while i < n:

    if not stack or arr[stack[-1]] <= arr[i]:
        stack.append(i)
        i+= 1
    else:
        top = stack[-1]
        stack.pop()

        if not stack:
            curr = arr[top]*i
        else:
            curr = arr[top]*(i-stack[-1]-1)
        if curr > largest_area:
            largest_area = curr
while stack:
    top = stack[-1]
    stack.pop()
    if not stack:
        curr = arr[top]*i
    else:
        curr = arr[top]*(i-stack[-1]-1)
    if curr > largest_area:
        largest_area = curr
return largest_area

