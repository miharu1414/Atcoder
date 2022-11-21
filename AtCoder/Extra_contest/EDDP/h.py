h,w = map(int,input().split())
a = [input() for i in range(h)]
mod = 1000000007
dp = [[0]*(w+1) for i in range(h+1)]
dp[0][0] = 1
for i in range(h):
    for j in range(w):
        if a[i][j] == '#':
            continue
        if i < h-1: 
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= mod
        if j < w-1:
            dp[i][j+1] += dp[i][j]
            dp[i][j+1] %= mod

print(dp[h-1][w-1])