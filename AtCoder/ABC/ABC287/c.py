n, m = map(int,input().split())
u,v =  [],[]
import sys
sys.setrecursionlimit(10**6)
from collections import deque

edge = []

G = [[] for i in range(n)]
into_num = [0]*n

for i in range(m):
    a,b = map(int,input().split())
    u.append(a-1)
    v.append(b-1)
    G[a-1].append(b-1)
    G[b-1].append(a-1)
    into_num[a-1] += 1
    into_num[b-1] += 1
    edge.append((a,b))

start = -1
for i in range(n):
    if len(G[i]) == 1:
        start = i
        break

seen = [0]*n
def dfs(v,p):
    seen[v] = 1
    cnt = 0
    for nv in G[v]:
        if nv == p: continue
        else:
            if seen[nv] == 1: return False
            else:
                dfs(nv,v)
                cnt += 1
    if cnt >1: return False
    return True

if dfs(start,-1):
    for i in range(n):
        if seen[i] != 1:
            print("No")
            exit()
    print("Yes")
else:
    print("No")
