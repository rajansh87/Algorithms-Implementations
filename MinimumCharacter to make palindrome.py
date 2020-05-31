#tt=int(input())
#for qwerty in range(tt):
    #n=input()
    #n=int(n)
    #n,k=map(int,input().split()) 
    #arr=list(map(int,input().split()))
s="ABC"
#iiijiiiii


cnt = 0
flag = 0
  
while(len(s) > 0): 
  
    # if string becomes palindrome then break 
    if(s==s[::-1]): 
        flag = 1
        break
      
    else: 
        cnt += 1
      
        # erase the last element of the string 
        s = s[:-1] 
  
# print the number of insertion at front 
if(flag): 
    print(cnt) 
        
