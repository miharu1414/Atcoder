n,m = map(int,input().split())
b = [list(map(int,input().split())) for i in range(n)]

flag = 1
d_up = 0
for column in range(m):

    for row in range(n-1):
        if b[row+1][column] != b[row][column] + 7 : 

            flag= 0
for row in range(n):
    
    for column in range(m-1):
        if b[row][column+1] != b[row][column] + 1 or ((b[row][column+1]-1)%7  < (b[row][column]-1)%7 ):
            flag = 0
if flag:
    print("Yes")
else:
    print("No")