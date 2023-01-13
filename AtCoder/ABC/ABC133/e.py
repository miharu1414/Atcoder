import sys
sys.setrecursionlimit(10**6)

n, k = map(int,input().split())
a, b = [], []
G = [[] for i in range(n)]
for i in range(n-1):
    x, y = map(int,input().split())
    a.append(x-1)
    b.append(y-1)
    G[y-1].append(x-1)
    G[x-1].append(y-1)

def dfs(v,p,now):
    seen[v] = 1
    if p != -1:
        now += 1
        if pre[p] != -1:
            now += 1
    ans[v] = now
    pre[v] = p
    now = 0
    for nv in G[v]:
        if seen[nv]: continue
        dfs(nv,v,now)
        now += 1

seen = [0]*n
pre = [-1]*n
ans = [0]*n
start = [-1,-1]
for i in range(n):
    if start[1] < len(G[i]):
        start[1] = len(G[i])
        start[0] = i


dfs(start[0],-1,0)
mod = 10**9 + 7
Answer = 1
for i in range(n):
    Answer = (Answer * (k - ans[i]))%mod
print(Answer)