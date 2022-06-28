n = int(input())
G = [[] for i in range(n+1)]
ab = [map(int,input().split()) for i in range(n-1)]
a,b = [list(i) for i in zip(*ab)]

for i in range(n-1):
    G[a[i]-1].append(b[i]-1)
    G[b[i]-1].append(a[i]-1)

dist = [-1]*n
dist[0] = 0

from collections import deque
deq = deque()

deq.append(0)
while len(deq):
    now = deq.popleft()
    for v in G[now]:
        if dist[v]!=-1:
            continue
        dist[v] = dist[now] + 1
        deq.append(v)

max_i = 0
max_dist = 0
for i in range(len(dist)):
    if dist[i]>max_dist:
        max_dist = dist[i]
        max_i = i

dist=[-1]*n
dist[max_i] = 0
deq = deque()
deq.append(max_i)
while len(deq):
    now = deq.popleft()
    for v in G[now]:
        if dist[v]!=-1:
            continue
        dist[v] = dist[now] + 1
        deq.append(v)

print(max(dist)+1)
