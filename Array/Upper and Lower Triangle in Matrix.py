arr=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

n=4#row
m=4#col

#print matrix lower triangle and upper triangle
print("Lower Triangle")
for i in range(n):        
    for j in range(0,i+1):
        print(arr[i][j],end=" ")
    print()

print("Upper Triangle")
for i in range(m):
    for j in range(0,n-i):
        print(arr[i][j],end=" ")
    print()
