n, k = map(int,input().split())
a = list(map(int,input().split()))

dp = [[0]*200002 for i in range(102)]
mod = 10**9+7
for i in range(a[0]+1):
    dp[0][k-i] = 1
for i in range(1,n):
    ruiseki = 0
    for j in range(a[i]+1):
        ruiseki += dp[i-1][j]
    ruiseki %= mod
    for j in range(k+1):
        dp[i][j] += ruiseki
        ruiseki -= dp[i-1][j]
        ruiseki += dp[i-1][j+a[i]+1]
        dp[i][j] %= mod
        ruiseki %= mod
print(dp[n-1][0])