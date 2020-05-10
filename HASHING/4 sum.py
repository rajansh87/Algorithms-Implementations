arr=[1,0,-1,0,-2,2]
target=0

def four_sum( arr, target):
    hash_map = dict()
    arr.sort()
    result = set()

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            curr_sum = arr[i] + arr[j]
            diff = target - curr_sum
            if diff in hash_map:
                for prev_sum in hash_map[diff]:
                    if arr[prev_sum[1]] <= arr[i] and i > prev_sum[1]:
                        result.add((arr[prev_sum[0]], arr[prev_sum[1]], arr[i], arr[j]))

            if curr_sum in hash_map:
                hash_map[curr_sum].append((i, j))
            else:
                hash_map[curr_sum] = [(i, j)]

    return sorted([list(item) for item in result])                
    
    

