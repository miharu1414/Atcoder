# スタックオーバーフローを防ぐ
import sys
sys.setrecursionlimit(10 ** 6)

n, m = map(int,input().split())
G = [[] for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)
dist = [-1] * n
nodes = [[] for i in range(n)]


dist[0] = 0
nodes[0] = [0]
for k in range(1,n):
    for v in nodes[k-1]:
        for next_v in G[v]:
            if dist[next_v] != -1:
                continue
            
            dist[next_v] = dist[v] + 1
            nodes[k].append(next_v)
            