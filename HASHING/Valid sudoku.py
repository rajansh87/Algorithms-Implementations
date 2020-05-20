arr= [ "..4...63.", ".........", "5......9.", "...56....", "4.3.....1", "...7.....", "...5.....", ".........", "........." ]

import numpy as np


z=0

brr=[1,2,3,4,5,6,7,8,9]
sudoku=[[0 for i in range(9)] for j in range(9)]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]!=".":
            sudoku[i][j]=int(arr[i][j])
game=np.array(sudoku)
for i in range(len(sudoku)):
    for j in range(len(sudoku[i])):
        if sudoku[i][j]!=0:
            num=sudoku[i][j]
            #print(num)
            if((np.count_nonzero(game[i,:]==num)>1)or(np.count_nonzero(game[:,j]==num)>1)):
                    print(0)
                    z=1
                    break
    if z==1:
        break     

a1=game[0:3,0:3]
a2=game[0:3,3:6]
a3=game[0:3,6:9]
a4=game[3:6,0:3]
a5=game[3:6,3:6]
a6=game[3:6,6:9]
a7=game[6:9,0:3]
a8=game[6:9,3:6]
a9=game[6:9,6:9]

c=[0]*10
zero=0
for i in range(3):
    for j in range(3):
        if a1[i][j]==0:
            zero+=1
        else:
            c[a1[i][j]]+=1
if c.count(1)+zero!=9:
    print(0)
c=[0]*10
zero=0
for i in range(3):
    for j in range(3):
        if a2[i][j]==0:
            zero+=1
        else:
            c[a2[i][j]]+=1
if c.count(1)+zero!=9:
    print(0)
c=[0]*10
zero=0
for i in range(3):
    for j in range(3):
        if a3[i][j]==0:
            zero+=1
        else:
            c[a3[i][j]]+=1
if c.count(1)+zero!=9:
    print(0)
c=[0]*10
zero=0
for i in range(3):
    for j in range(3):
        if a4[i][j]==0:
            zero+=1
        else:
            c[a4[i][j]]+=1
if c.count(1)+zero!=9:
    print(0)
c=[0]*10
zero=0
for i in range(3):
    for j in range(3):
        if a5[i][j]==0:
            zero+=1
        else:
            c[a5[i][j]]+=1
if c.count(1)+zero!=9:
    print(0)

c=[0]*10
zero=0
for i in range(3):
    for j in range(3):
        if a6[i][j]==0:
            zero+=1
        else:
            c[a6[i][j]]+=1
if c.count(1)+zero!=9:
    print(0)
c=[0]*10
zero=0
for i in range(3):
    for j in range(3):
        if a7[i][j]==0:
            zero+=1
        else:
            c[a7[i][j]]+=1
if c.count(1)+zero!=9:
    print(0)
c=[0]*10
zero=0
for i in range(3):
    for j in range(3):
        if a8[i][j]==0:
            zero+=1
        else:
            c[a8[i][j]]+=1
if c.count(1)+zero!=9:
    print(0)
c=[0]*10
zero=0
for i in range(3):
    for j in range(3):
        if a9[i][j]==0:
            zero+=1
        else:
            c[a9[i][j]]+=1
if c.count(1)+zero!=9:
    print(0)

        
print(1)
             
                
                    
                
            





                
                
                    
                
            




