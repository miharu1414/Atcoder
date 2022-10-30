n,m,k = map(int,input().split())

mod =  998244353 
dp = [[0]*(n+1) for i in range(k+1)]

dp[0][0] = 1
S = 0
minv = pow(m,-1,mod)
for i in range(k):
    for j in range(n):
        for l in range(1,m+1):
            if j + l <= n:
                dp[i+1][j+l] += dp[i][j]*minv 


            elif j + l > n :
                dp[i+1][n - (j+l-n)] += dp[i][j]*minv

    dp[i+1][j] += dp[i][j]

sum = 0

print(dp[k][n])