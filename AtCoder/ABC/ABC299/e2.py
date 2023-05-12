from collections import deque

# 入力
N, M = map(int, input().split())
edges = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    edges[u-1].append(v-1)
    edges[v-1].append(u-1)
K = int(input())
p = list(map(int, input().split()))
d = list(map(int, input().split()))

# BFS で最短距離を求める
dist = [float('inf') for _ in range(N)]
for i in range(K):
    p[i] -= 1
    dist[p[i]] = 0
q = deque(p)
while q:
    v = q.popleft()
    for u in edges[v]:
        if dist[u] == float('inf'):
            dist[u] = dist[v] + 1
            q.append(u)
for i in range(N):
    if dist[i] <= d[min(K-1, dist[i])]:
        dist[i] = 0
    else:
        dist[i] = 1

# 黒で塗られた頂点があるかを確認
if sum(dist) > 0:
    print('1')
    print(' '.join(str(1 if dist[i] == 0 else 2) for i in range(N)))
else:
    print('-1')
