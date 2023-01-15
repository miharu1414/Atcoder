n = int(input())
ab = [map(int,input().split()) for i in range(n-1)]
a,b = [list(i) for i in zip(*ab)]

G = [[] for i in range(n)]
for i in range(n-1):
    G[a[i]-1].append(b[i]-1)
    G[b[i]-1].append(a[i]-1)


start = [-1,0]
for i in range(n-1):
    if len(G[i]) > start[1]:
        start = i,len(G[i])


def sort_idx(x,y):
    if x <= y:
        return x,y
    else:
        return y,x

seen = [0]*n
color = dict()

max_n = start[1]
from collections import defaultdict
d = defaultdict(set)
def dfs(v,p):
    seen[v] = 1
    if p != v:
        now = 0
        for i in range(1,max_n+1):
            if i not in d[p]:
                now = i 
                break
        color[sort_idx(v,p)] = now
        d[p].add(now)
        d[v].add(now)

        cnt = 0
    for nv in G[v]:
        if seen[nv] == 1: continue
        dfs(nv,v)

dfs(start[0],start[0])
print(max_n)
for i in range(n-1):
    print(color[sort_idx(a[i]-1,b[i]-1)])
        
    
    