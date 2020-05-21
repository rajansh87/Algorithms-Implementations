S= "ADOBECODEBANC"
T= "ABC"


import collections as coll
need, missing = coll.Counter(T), len(T)

I = J = i = 0
for j, c in enumerate(S,1):
    missing -= need[c] > 0
    need[c] -= 1
    if not missing:
        while i < j and need[S[i]] < 0:
            need[S[i]] += 1
            i += 1
        if not J or j -i < J - I:
            J, I = j, i


print( S[I:J])
