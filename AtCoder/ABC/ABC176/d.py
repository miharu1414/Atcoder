h, w = map(int,input().split())
sy,sx = map(int,input().split())
gy,gx = map(int,input().split())

s = [input() for i in range(h)]
sy-=1
sx-=1
gy-=1
gx-=1

from collections import deque
deq = deque([])
dist = [[-1]*w for i in range(h)]

X = [0,0,1,-1]
Y = [1,-1,0,0]
dist[gy][gx] = 0
X1 = [0,2,0,-2,1,-1,1,-1,2,2,2,2,-2,-2,-2,-2,1,-1,1,-1]
Y1 = [2,0,-2,0,1,1,-1,-1,1,-1,2,-2,1,-1,2,-2,2,2,-2,-2]
deq.append([gy,gx])

while len(deq):
    v = deq.popleft()
    y,x = v
    for dx,dy in zip(X,Y):
        
        if  w > x+dx and x+dx >=0 and h > y+dy and y+dy>=0 and s[y+dy][x+dx]=="." and (dist[y+dy][x+dx] == -1 or dist[y+dy][x+dx] > dist[y][x] ) :
            dist[y+dy][x+dx] = dist[y][x] 
            deq.append([y+dy,x+dx])
    for dx,dy in zip(X1,Y1):
        if w > x+dx and x+dx >=0 and h > y+dy and y+dy>=0 and  s[y+dy][x+dx]=="." and (dist[y+dy][x+dx] == -1 or dist[y+dy][x+dx] > dist[y][x] + 1 ):
            dist[y+dy][x+dx] = dist[y][x]+1 
            deq.append([y+dy,x+dx])
print(dist[sy][sx])