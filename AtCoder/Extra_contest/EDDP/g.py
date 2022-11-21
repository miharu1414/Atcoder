n, m = map(int,input().split())
xy = [map(int,input().split()) for i in range(m)]
x,y = [list(i) for i in zip(*xy)]

G =[[] for i in range(200001) ]

dim = [0]*200001
for i in range(m):
    G[x[i]].append(y[i])
    dim[y[i]] += 1

for i in range(1,n+1):
    G[i].sort()
from collections import deque
d = deque()
for i in range(1,n+1):
    if dim[i] == 0:
        d.append(i)

ans = []
while len(d) > 0:
    now = d.popleft()
    for nv in G[now]:
        dim[nv] -= 1
        if dim[nv] ==0:
            d.append(nv)
    ans.append(now)
# print(ans)

dp = [0]*200001
for i in ans:
    for v in G[i]:
        dp[v] = max(dp[v],dp[i]+1)
print(max(dp))
    
        
    
    