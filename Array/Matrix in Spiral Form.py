arr=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

n=4#col
m=4#row

#print matrix in spiral form
loop=0
while(loop<n/2):
    for i in range(loop,n-loop-1):
        print(arr[loop][i],end=" ")
    for i in range(loop,m-loop-1):
        print(arr[i][m-loop-1],end=" ")
    for i in range(n-1-loop,loop-1+1,-1):
        print(arr[m-loop-1][i],end=" ")
    for i in range(m-loop-1,loop,-1):
        print(arr[i][loop],end=" ")
    loop+=1


        
