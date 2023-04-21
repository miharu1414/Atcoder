n = int(input())
ab = [map(int,input().split()) for i in range(n)]
a,b = [list(i) for i in zip(*ab)]

dp = [[0,0] for i in range(n)]
MOD = 998244353 
for i in range(n):
    if i == 0:
        dp[i][0] = 1
        dp[i][1] = 1
        continue
    for j in range(2):
        if j%2:
            if a[i] != a[i-1]:
                dp[i][j] += dp[i-1][j]
            if a[i] != b[i-1]:
                dp[i][j] += dp[i-1][~j]
        else:
            if b[i] != a[i-1]:
                dp[i][j] += dp[i-1][~j]
            if b[i] != b[i-1]:
                dp[i][j] += dp[i-1][j]
        dp[i][j] %= MOD
print(sum(dp[n-1])%MOD)
        