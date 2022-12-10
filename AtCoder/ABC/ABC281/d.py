n,k,d = map(int,input().split())
a = list(map(int,input().split()))
dp = [[[-1]*(d) for i in range(k+1)] for i in range(n+1)]

for i in range(n):
    dp[i][0][0] = 0
for i in range(1,n+1):
    for j in range(1,k+1):
        for l in range(d):
            # A_iを採用しない
            if(dp[i-1][j][l]!=-1):  dp[i][j][l] = max(dp[i][j][l],dp[i-1][j][l])
            
            # A_iを採用する
            if(dp[i-1][j-1][(l-a[i-1])%d]!=-1): dp[i][j][l] = max(dp[i][j][l],dp[i-1][j-1][(l-a[i-1])%d]+a[i-1])
            
print(dp[n][k][0])
            
            