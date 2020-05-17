s="abcabcbb"

if len(s) < 2:
    print(len(s))
else:
    n, d = len(s), {}
    d[s[0]] = 0
    p1 = 0
    p2 = 1
    max_length = 1
    while p2 < n:
        if s[p2] in d and p1 <= d[s[p2]]:
            p1 = d[s[p2]] + 1
        else:
            max_length = max(p2 - p1+1, max_length)
        d[s[p2]] = p2
        p2 += 1
    print( max_length)
