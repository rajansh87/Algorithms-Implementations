#tt=int(input())
#for qwerty in range(tt):
    #n=input()
    #n=int(n)
    #n,k=map(int,input().split()) 
    #arr=list(map(int,input().split()))
A=[10,-1,2,3,-4,100]

def maxset(A):
    n = 0
    i = 0
    ans =-99999999999999999999
    index = []
    while i< len(A):
        start = i
        end = start
        summ = 0

        while i < len(A) and A[i]>=0:
            summ += A[i]
            end += 1
            i += 1
        if summ > ans:
            ans = summ
            index.append([start, end])
            n +=1
        i +=1
    return A[index[n-1][0]:index[n-1][1]]
print(maxset(A))
