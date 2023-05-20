from collections import defaultdict


# 入力例
N, M = map(int, input().split())
sets = []


# 深さ優先探索（行きがけ）
import sys

from collections import deque
n = N
num_pos = [[] for i in range(M)]

# グラフの作成(無向グラフでは#を消す)
graph = [deque([]) for _ in range(N + 1)]

A = []
for idx in range(N):
    a = int(input())
    A.append(a)
    S = list(map(int, input().split()))
    for i in range(a):
        num_pos[S[i]-1].append(idx)
    Ss = []
    for s in S:
        Ss.append(s-1)
    sets.append(Ss)
st = set()
for num in num_pos[0]:
    for atai  in sets[num]:
        st.add(atai)
try:
    sets[num_pos[0][0]]=list(st)
except:
    print(-1)

    


dist = [-1] * (n+1)
dist[0] = 0

d = deque()
d.append(0)

while d:
    v = d.popleft()
    for k in sets[v]:

        
        for i in num_pos[k]:
            if dist[i] != -1 or i == v:
                continue
            dist[i] = dist[v] + 1
            d.append(i)

ans = []
for i in num_pos[M-1]:
    ans.append(i)
sr = 1<<60
for i in ans:
    if dist[i]!=-1:
        sr = min(sr,dist[i])
if sr==1<<60:
    print(-1)
else:
    print(sr)