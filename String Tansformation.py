# to convert p into q by applying min number of operations:
# operation -> bring any selected character to the front of string.
tt=int(input())
for qwerty in range(tt):
    #n=input()
    #n=int(n)
    #n,k=map(int,input().split()) 
    #arr=list(map(int,input().split()))
    p,q=input().split()
    freq1=[0]*27    
    freq2=[0]*27
    for i in p:
        freq1[ord(i)-65]+=1
    for i in q:
        freq2[ord(i)-65]+=1
        
    if freq1!=freq2:
        print(-1)
    else:
        i=len(p)-1
        c=0
        j=i
        while i>=0:
            while p[i]!=q[j] and i>=0:
                i-=1
                c+=1
            if i>=0:
                i-=1
                j-=1
        print(c)
        
    
