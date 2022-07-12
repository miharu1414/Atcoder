h,w  = map(int,input().split())
s = [input() for i in range(h)]
G = [[0]*w for i in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            G[i][j] = 1


x = [1,0,0,-1]
y = [0,1,-1,0]

def rec(v1,v2):
    G[v1][v2] = 0
    for dx,dy in zip(x,y):
        if v1 + dx <0 or v1 +dx >=h or v2 +dy <0 or v2 + dy >= w:
            continue
        if  G[v1 + dx][v2+dy] == 0:
             continue
        rec(v1+dx,v2+dy)

cnt  = 0
for i in range(h):
    for j in range(w):
        if G[i][j] == 1:
            rec(i,j)
            cnt += 1

print(cnt)