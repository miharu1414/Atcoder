import sys
sys.setrecursionlimit(10 ** 6)

n,m,s,t = map(int,input().split())
G = [[]for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    G[a].append(b)

from collections import deque

d = deque()
d.append(s)

seen = [-1] * n
pre  = [0] * n 
while len(d):
    now = d.popleft()


    for next_v in G[now]:
        if seen[next_v] != -1:
            continue
        seen[next_v] = 1
        pre[next_v] = now
        d.append(next_v)


v = t
path = [v]
while v != s:
    v = pre[v]
    path.append(v)

ans = list(reversed(path))
print(*ans)
