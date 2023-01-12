# スタックオーバーフローを防ぐ
import sys
sys.setrecursionlimit(10 ** 6+100)
n,m = map(int,input().split())
u,v =  [],[]
G = [[] for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)


seen = [0]*n
ans = 0 

def dfs(x):
    global ans 
    seen[x] = 1
    ans += 1
    if ans >= 10**6:
        print(10**6)
        exit()
    for nx in G[x]:
        if seen[nx]!=1:
            dfs(nx)
    seen[x] = 0
dfs(0)
print(ans)