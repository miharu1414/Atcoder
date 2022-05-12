n = int(input())
a = [list(map(int,input().split())) for i in range(n)]
m = int(input())
G = [[1]*n for i in range(n)]
for i in range(m):
    x,y = map(int,input().split())
    G[x-1][y-1]=0
    G[y-1][x-1]=0


import itertools
t = [i for i in range(n)]
count = 1<<30
ok = 0
for run in itertools.permutations(t):
    possible = 1
    cost = a[run[0]][0]
    for i in range(n-1):
        cost += a[run[i+1]][i+1]
        if G[run[i+1]][run[i]]==0:
            possible = 0
            break 
            
    if possible:
        count = min(count,cost)
        ok = 1

if ok:
    print(count)
else:
    print(-1)
    