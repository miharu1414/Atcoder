h, w = map(int,input().split())
start_x, start_y, goal_x, goal_y = map(int,input().split())
s = [input() for i in range(h)]


from collections import deque
deq = deque([])

deq.append([start_x,start_y])

dx1 = [-1,1,0,0]
dy1 = [0,0,1,-1]

dist = [[-1]*w for i in range(h)]
dist[start_x][start_y] = 0

while len(deq):
    now_x , now_y = deq.popleft()
    for dx,dy in zip(dx1,dy1):
        x = now_x + dx
        y = now_y + dy
        
        if x<0 or y < 0 or x>=h or y >= w or s[x][y] =='B':
            continue
        if dist[x][y] != -1:
            continue
        dist[x][y] = dist[now_x][now_y] +1
        deq.append([x,y])

print(dist[goal_x][goal_y])
        