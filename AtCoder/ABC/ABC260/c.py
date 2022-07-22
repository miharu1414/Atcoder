n,x,y = map(int,input().split())

dp = [[0]*2 for i in range(n+1)]
dp[n][0] = 1
for i in range(n,1,-1):
    for j in  range(2):
        if j == 0:
            dp[i-1][j] += dp[i][j]
            dp[i][j+1] += x*dp[i][j]

        else:
            dp[i-1][j-1] += dp[i][j]
            dp[i-1][j] += y*dp[i][j]
print(dp[1][1]) 