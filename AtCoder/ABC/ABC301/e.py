dx = [1,0,-1,0]
dy = [0,1,0,-1]

from collections import deque 
def bit_count(number):
    count = 0
    while number:
        count += number & 1
        number >>= 1
    return count

def bfs(a,sx,sy):
    h = len(a)
    w = len(a[0])
    dist = [[-1 for i in range(w)] for i in range(h) ]
    d = deque([])
    
    dist[sx][sy] = 0
    d.append([sx,sy])
    
    while len(d):
        x, y = d.popleft()
        
        for i in range(4):
            x2 = x + dx[i]
            y2 = y + dy[i]
            if x2 < 0 or x2 >= h or y2 < 0 or y2 >= w:
                continue
            if a[x2][y2] == '#':
                continue
            
            if dist[x2][y2] == -1:
                dist[x2][y2] = dist[x][y] + 1
                d.append([x2,y2])
    
    return dist

INF = 1<<60

h, w ,t = map(int, input().split())
a = []
for i in range(h):
    a1 = input()
    a.append(a1)
    
nodes = []
start = -1
goal = -1
for i in range(h):
    for j in range(w):
        if a[i][j] == 'S':
            start = len(nodes)
            nodes.append([i,j])
        elif a[i][j] == 'G':
            goal = len(nodes)
            nodes.append([i,j])
        elif a[i][j] == 'o':
            nodes.append([i,j])
n = len(nodes)

G = [[INF for i in range(n)] for j in range(n) ]
for i in range(n):
    x, y = nodes[i]
    dist = bfs(a,x,y)
    for j in range(n):
        x2, y2 = nodes[j]
        if dist[x2][y2] != -1:
            G[i][j] = dist[x2][y2]
dp = [[INF for i in range(n)] for j in range(1<<n)]
dp[1<<start][start] = 0
for bit in range(1<<n):
    for v in range(n):
        for v2 in range(n):
            nbit = bit | (1<<v2)
            dp[nbit][v2] = min(dp[nbit][v2], dp[bit][v] + G[v][v2])

res = -1
for bit in range(1<<n):
    if dp[bit][goal] <= t:
        res = max(res, bit_count(bit) - 2)
print(res)
