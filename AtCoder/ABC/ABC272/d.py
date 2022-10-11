n,m = map(int,input().split())

pair = []

pat = dict()
i = 0
while i * i <= m:
    j = 0
    while i*i + j*j <= m:
        if i*i + j*j == m:

            if (i,j) not in pat:
                pat[(i,j)] = 1
                pair.append([i,j])
            if (i,-j) not in pat:
                pat[(i,-j)] = 1
                pair.append([i,-j])
            if (-i,j) not in pat:
                pat[(-i,j)] = 1
                pair.append([-i,j])
            if (-i,-j) not in pat:
                pat[(-i,-j)] = 1
                pair.append([-i,-j])
        j += 1
    i+=1


dist = [[-1]*n for i in range(n)]

dist[0][0] = 0
from collections import deque


d = deque()
d.append([0,0])

while len(d):
    now_x, now_y = d.popleft()
    for dx,dy in pair:
        next_x = now_x +dx
        next_y = now_y +dy
        if next_x >= n or next_x <0 or next_y>=n or next_y <0:
            continue
                    
        if dist[next_x][next_y] == -1:
            dist[next_x][next_y] = dist[now_x][now_y] + 1
            d.append([next_x,next_y])
        else:
            dist[next_x][next_y] = min(dist[next_x][next_y],dist[now_x][now_y] + 1)
        
for i in range(n):
    print(*dist[i])