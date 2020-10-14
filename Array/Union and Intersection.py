arr1=[1,2,3,4,5]
arr2=[4,5,6,7,8]

#Union and Intersection

union=[]
i=0
j=0
while i<len(arr1) and j<len(arr2):
    if arr1[i]<arr2[j]:
        union.append(arr1[i])
        i+=1 
        
    elif arr1[i]>arr2[j]:
        union.append(arr2[j])
        j+=1
        
    else:
        union.append(arr1[i])
        union.append(arr2[j])
        i+=1
        j+=1


if i!=len(arr1):
    union+=arr1
elif j!=len(arr2):
    union+=arr2
print("UNION : ",union)
######

intersection=[]
i=0
j=0
while i<len(arr1) and j<len(arr2):
    if arr1[i]<arr2[j]:
        i+=1 
        
    elif arr1[i]>arr2[j]:
        j+=1
        
    else:
        intersection.append(arr1[i])
        i+=1
        j+=1

print("Intersection : ",intersection)



