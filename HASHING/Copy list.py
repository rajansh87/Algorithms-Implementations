from collections import defaultdict
d = defaultdict(lambda: RandomListNode(0))
d[None] = None
m = head

while m:
    d[m].label = m.label
    d[m].next = d[m.next]
    d[m].random = d[m.random]
    m = m.next
    
return d[head]
