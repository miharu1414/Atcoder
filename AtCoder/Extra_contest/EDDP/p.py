# スタックオーバーフローを防ぐ
import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
x,y = [],[]
G = [[]for i in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)

start = 0
for i in range(n):
    if len(G[i]) == 1:
        start=i
        break

seen = [0]*n

dp = [[0,0]for i in range(n)] 
def dfs(v,p):
    seen[v] = 1
    flag = 1
    white,black = 1,1
    for nv in G[v]:
        if seen[nv]==1 or nv == p:
            continue
        
        w,b = dfs(nv,v)
        flag = 0
        white *= (w+b)
        black *= w
    if flag:
        dp[v] = [1,1]

    else:
        dp[v][0] = white
        dp[v][1] = black

    return dp[v]

print(sum(dfs(start,-1)))