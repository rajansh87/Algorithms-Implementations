def slidingMaximum(self, arr,w):
    
    n = len(arr)
    from collections import deque
    lookup = deque()
    if w >= n:
        return [max(arr)]
    res = []
    for i in range(n):
        while lookup and arr[i] >= arr[lookup[-1]]:
            lookup.pop()
        lookup.append(i)
        if i >= w and lookup and lookup[0] == i - w:
            lookup.popleft()
        if i >= w -1:
            res.append(arr[lookup[0]])
    return res

    
