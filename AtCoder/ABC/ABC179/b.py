n = int(input())
d = [list(map(int,input().split())) for i in range(n)]

cnt = 0
for i in range(n):
    
    if d[i][0] == d[i][1]:
        zorome = 1
    else:
        zorome = 0
    if zorome:
        cnt+=1
    else:
        cnt=0
    if cnt ==3:
        print("Yes")
        exit()
print("No")
    