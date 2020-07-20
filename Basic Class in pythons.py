##tt=int(input())
##for qwerty in range(tt):
##    n=int(input())
##    #s,n=map(int,input().split())
##    arr=list(map(int,input().split()))            
##


class Car:
    mspeed=0
    sunit=""
    s=""
    def __init__(self,mspeed,sunit):
        self.mspeed=mspeed
        self.sunit=sunit
        
    def __str__(self):
        return "Car with the maximum speed is "+str(self.mspeed)+" "+str(self.sunit)

class Boat:
    mspeed=0
    s=""
    def __init__(self,mspeed):
        self.mspeed=mspeed
        s="Boat with the maximum speed of "+str(self.mspeed)+" knots"
    def __str__(self):
        return "Boat with the maximum speed of "+str(self.mspeed)+" knots"

o1=Car(4,"km/h")
o2=Boat(5)
