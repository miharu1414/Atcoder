n, a, b, p, q = map(int,input().split())
dp = [[[0 for k in range(2)] for i in range(n+1)] for j in range(n+1)]
MOD = 998244353
for i in range(n):
    for f in range(2):
        dp[n][i][f] = 1
        dp[i][n][f] = 0
    
for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        for k in range(1,p+1):
            dp[i][j][0] = (dp[i][j][0]+dp[min(n,i+k)][j][1])%MOD
        dp[i][j][0] = (dp[i][j][0]*pow(p,-1,MOD))%MOD
        for k in range(1,q+1):
            dp[i][j][1] = (dp[i][j][1]+dp[i][min(n,j+k)][0])%MOD
        dp[i][j][1] = (dp[i][j][1]*pow(q,-1,MOD))%MOD

print(dp[a][b][0])