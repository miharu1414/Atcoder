n,x,y = map(int,input().split())
a = list(map(int,input().split()))

g1 = []
g2 = []
for i in range(n):
    if i&1:
        g2.append(a[i])
    else:
        g1.append(a[i])

tyouten = []
now_x,now_y = 0,0
num_y = 0
num_x = 0

zahyou = []
for i in range(n):
    if i&1:
        now_y += g2[num_y]
        num_y += 1
    else:
        now_x += g1[num_x]
        num_x += 1
    zahyou.append((now_x,now_y))

dp_x = [[0]*(2*10**4+1) for i in range(n+1)]
dp_y = [[0]*(2*10**4+1) for i in range(n+1)]

dp_x[1][g1[0]+10**4] = 1
dp_y[0][10**4] = 1

for i in range(1,num_x):
    for j in range(2*10**4+1):
        if j+g1[i]>=0 and j+g1[i] < 2*10**4+1:
            dp_x[i+1][j+g1[i]] += dp_x[i][j] 
        if j-g1[i] >=  0:
            dp_x[i+1][j-g1[i]] += dp_x[i][j] 
        
for i in range(num_y):
    for j in range(2*10**4+1):
        if j+g2[i] < 2*10**4+1:
            dp_y[i+1][j+g2[i]] += dp_y[i][j]
        if j-g2[i] >= 0:
            dp_y[i+1][j-g2[i]] += dp_y[i][j]
        
if dp_x[num_x][x+10**4] and dp_y[num_y][y+10**4]:
    print("Yes")
else:
    print("No")