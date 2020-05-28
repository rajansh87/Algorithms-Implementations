#tt=int(input())
#for qwerty in range(tt):
    #n=input()
    #n=int(n)
    #n,k=map(int,input().split()) 
    #arr=list(map(int,input().split()))
s="AAA"

ans=0
for i in range(len(s)):
    ans=26*ans+ord(s[i])-65+1
print(ans)
