n = int(input())
if n ==1:
    print(2)
    exit()
xy = [map(int,input().split()) for i in range(n-1)]
x,y = [list(i) for i in zip(*xy)]

dp = [[0,0] for i in range(n+1)]
G = [[] for i in range(n+1)]

for i in range(n-1):
    G[x[i]].append(y[i])
    G[y[i]].append(x[i])

is_seen = [0]*(n+1)
def dfs(v):
    
    is_seen[v] = 1
    flag=  1
    black = 1
    white = 0
    for next_v in G[v]:
        if is_seen[next_v] == 0:
            flag = 0
            b,w = dfs(next_v)
            
            black *= w
            white += w + b
    if flag:
        black = 1
        white = 1
    dp[v][0] = black
    dp[v][1] = white
    print(black,white)
    return black,white
start = 0
for i in range(1,n+1):
    if len(G[i]) == 1:
        start = i
        break
dfs(start)
print(sum(dp[start]))