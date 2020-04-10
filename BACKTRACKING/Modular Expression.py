def Mod(x,n,m):
    if(x==0):
        return 0
    elif(n==0):
        return 1
    elif(n%2==0):
        y=Mod(x,n//2,m)#when inside class use self.Mode
        return (y*y)%m
    else:
        y=Mod(x,n-1,m)#when inside class use self.Mode
        return ((x%m)*y)%m
print(Mod(2,3,3))
