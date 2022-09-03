n,m = map(int,input().split())
a =list(map(int,input().split()))

dp = [[-(10**12)]*(m+1)  for i in range(n+1)]

# dp[i][j] : i桁まで見て，j個選んだ時の最大値
for i in range(n-1,-1,-1):
    for j in range(0,m+1):
        if j == 0:
            dp[i][j] = 0
        if i < m - j:
            dp[i][m-j] = -(10**18)
        dp[i][j] = max(dp[i+1][j],dp[i+1][j-1] + (m+1-j)*a[i])
print(dp[0][m])