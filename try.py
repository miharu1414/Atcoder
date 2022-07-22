n,m,s,t = map(int,input().split())
ab = [map(int,input().split()) for i in range(m)]
a,b = [list(i) for i in zip(*ab)]

G = [[]for i in range(n)]

for i in range(m):
    G[a[i]].append(b[i])
visited = [0] *n


def rec(v):
    visited[v] = 1
    for next_v in G[v]:
        if visited[next_v]:
            continue
        rec(next_v)
rec(s)
if visited[t] == 1:
    print("Yes")
else:
    print("No") 

