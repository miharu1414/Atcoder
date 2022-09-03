# https://atcoder.jp/contests/abc266/tasks/abc266_f

# スタックオーバーフローを防ぐ
import sys
sys.setrecursionlimit(10 ** 6)
n = int(input())
G =[[] for i in range(n)]
deg = [0]*n
for i in range(n):
    u,v = map(int,input().split()) 
    u -= 1
    v -= 1
    G[v].append(u)
    G[u].append(v)
    deg[u]+=1
    deg[v] +=1

from collections import deque
from operator import neg

deq = deque()
root  = [-1] * n



for i in range(n):
    if len(G[i]) == 1:
        deq.append(i)


visited = [-1]*n

# 次数が1の頂点を消していく　=>残った頂点が閉路上の頂点

is_cicle = [1]*n
while len(deq):
    now = deq.popleft()
    visited[now] = 1
    is_cicle[now] = 0
    for next_v in G[now]:
        # 次数が1の頂点を消したときに次数が１になるなら
        if deg[next_v] >= 2:
            deg[next_v] -=1
            if deg[next_v] == 1:
                deq.append(next_v)





def dfs(v,p):
    root[v] = root[p]
    for next_v in G[v]:
        if next_v != p:
            dfs(next_v,v)
    

# 閉路上からdfs
for i in range(n):
    if is_cicle[i]:
        root[i] = i
        for v in G[i]:
            if not is_cicle[v]:
                dfs(v,i)

q = int(input())
for i in range(q):
    x,y = map(int,input().split())
    x-=1
    y-=1
    if root[x] == root[y]:
        print("Yes")
    else:
        print("No")

