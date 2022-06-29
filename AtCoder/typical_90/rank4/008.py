n = int(input())
s = input()
ans = "atcoder"
dp = [[0]*(len(ans)+1) for i in range(n+1)]
dp[0][0] = 1
mod = 10**9+7
for i in range(n):
    for j in range(len(ans)+1):
        if s[i] == "a":
            if j == 1:
                dp[i+1][j] = (dp[i+1][j]+dp[i][j-1])%mod
        elif s[i] == "t":
            if j ==2:
                dp[i+1][j]  = (dp[i+1][j]+dp[i][j-1])%mod
        elif s[i] == "c":
            if j == 3:
                dp[i+1][j]  = (dp[i+1][j]+dp[i][j-1])%mod
        elif s[i] == "o":
            if j == 4:
                dp[i+1][j]  = (dp[i+1][j]+dp[i][j-1])%mod
        elif s[i] == "d":
            if j == 5:
                dp[i+1][j] = (dp[i+1][j]+dp[i][j-1])%mod

        elif s[i] == "e":
            if j == 6:
                dp[i+1][j] = (dp[i+1][j]+dp[i][j-1])%mod
        elif s[i] == "r":
            if j == 7:
                dp[i+1][j]  = (dp[i+1][j]+dp[i][j-1])%mod
        dp[i+1][j] = (dp[i+1][j] + dp[i][j] )%mod
print(dp[n][7])
