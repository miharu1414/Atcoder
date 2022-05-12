from queue import Queue
h, w = map(int,input().split())
start_x,start_y, goal_x, goal_y = map(int,input().split())
s = [input() for i in range(h)]

dist = [[-1] * w for i in range(h)] 

que = Queue()

dist[start_x][start_y] = 0
que.put((start_x,start_y))

dx1 = [1,-1,0,0]
dy1 = [0,0,1,-1]

while not que.empty():
    next_x,next_y = que.get()

    for dx,dy in zip(dx1,dy1):
        x = next_x + dx
        y = next_y + dy
        if x < 0 or y < 0 or x >= h or y >= w or s[x][y] == 'B':
            continue
        if dist[x][y] != -1:
            continue
        dist[x][y] = dist[next_x][next_y] + 1
        que.put((x,y))

print(dist[goal_x][goal_y])