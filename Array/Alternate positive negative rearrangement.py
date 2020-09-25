arr=[1, 2, 3, -4, -1, 4]
n=len(arr)
#rearrange array with alternating positive negative elements

def func1(arr,n):        
    for i in range(n):
        if (arr[i]<0 and i%2!=0) or (arr[i]>0 and i%2==0):
            #outofplace
            temp=-1
            for j in range(i+1,n):
                if (arr[j]<0 and j%2!=0) or (arr[j]>0 and j%2==0):
                    if(arr[i]<0 and arr[j]>0) or (arr[i]>0 and arr[j]<0):
                        temp=j
                        break
            arr[i],arr[temp]=arr[temp],arr[i]
            
    print(arr)     
        
