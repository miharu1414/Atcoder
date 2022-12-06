n, p = map(int,input().split())
dp = [0]*100005

dp[n] = 0
for i in range(n-1,-1,-1):
    if i == n - 1:
        dp[i] = dp[i+1] + 1
        