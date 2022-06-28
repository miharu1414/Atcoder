from collections import deque
deq = deque()

n,m = map(int,input().split())
G =[[] for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)

dist = [-1]*n
dist[0] = 0
deq.append(0)
depth = [[] for i in range(n)]
depth[0].append(0)
while len(deq):
    v = deq.popleft()
    for next_v in G[v]:
        if dist[next_v] != -1:
            continue
        dist[next_v] = dist[v] +1
        deq.append(next_v)
        depth[dist[next_v]].append(next_v)

for i in range(len(depth)):
    depth[i].sort()
    print(*depth[i])
    