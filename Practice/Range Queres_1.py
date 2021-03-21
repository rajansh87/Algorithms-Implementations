# frequency of element in given range
import math

from collections import defaultdict as dict
#default stores keys in sorted form
from bisect import bisect_left as lower_bound
from bisect import bisect_right as upper_bound

def findFrequency(arr,n,left,right,element):
    #lower bound gives takes list of locations
    #where element is present in orgnal array
    #and the left range
    # and returns the index of element from
    #that list which is greater equal to given
    #left range.
    a=lower_bound(store[element],left)
    #upper bound gives takes list of locations
    #where element is present in orgnal array
    #and the right range
    # and returns the index of element from
    #that list which is less than or equal to
    #given right range.

    b=upper_bound(store[element],right)

    #return last index where element exists
    #in range - the first index where it
    #exist of the list of occurances

    return b-a 

arr=list(map(int,input("enter elements : ").split()))
n=len(arr)
store=dict(list)
for i in range(n):
    store[arr[i]].append(i+1)
#store consists of element as key and
#their locations of occurances in the
#given array as values

m=int(input("query size: "))
query=[]
for i in range(m):
    num=int(input("element : "))
    l,r=map(int,input("L,R :").split())
    print("frequency of ",num," in the range [",l,",",r,"] : ",
          findFrequency(arr,n,l,r,num))


    

