##tt=int(input())
##for qwerty in range(tt):
##    n=int(input())
##    #n,k=input().split()
##    #n,k=int(n),int(k)
##    #arr=list(map(int,input().split()))

n,q=input().split()
n,q=int(n),int(q)

arr=[0]*n
for query in range(q):    
    a,b,k=input().split()
    a,b,k=int(a),int(b),int(k)
    
    arr[a-1]+=k
    if b!=n:
        arr[b]-=k
    #print(arr)

ma=0
s=0
for i in range(len(arr)):
    s+=arr[i]
    if ma<s:
        ma=s
print(ma)
    
        
    

            
            
            
    
    

            
    
        

