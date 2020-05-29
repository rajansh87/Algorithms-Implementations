tt=int(input())
for qwerty in range(tt):
    #n=input()
    #n=int(n)
    #n,k=map(int,input().split()) 
    #arr=list(map(int,input().split()))       
    n=int(input())
    arr=list(map(int,input().split()))
    l,h=0,n-1
    arr.sort()
    mi=abs(arr[0]-arr[-1])
    m=[arr[0],arr[-1]]
    ans=[-1,-1]
    x=-1
    #print(arr)
    lo,hi=l,h
    while(l<h):
        lo,hi=l,h
        x=abs(0-(arr[lo]+arr[hi]))
        if arr[lo]+arr[hi]==0:
            ans=[arr[lo],arr[hi]]
            break
        elif arr[lo]+arr[hi]>0:
            h-=1
        else:
            l+=1
        
        #print(arr[lo],arr[hi])
        if x<mi:
            mi=abs(arr[lo]+arr[hi])
            m=[arr[lo],arr[hi]]
        #print("x:",x)
        #print(mi)
        #print(m)

    if ans==[-1,-1]:
        print(*m,sep=" ")
    else:
        print(*ans,sep=" ")
        
