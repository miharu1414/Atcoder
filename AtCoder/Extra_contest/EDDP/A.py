n = int(input())
h = list(map(int,input().split()))

dp = [2<<60]*(n+1)
dp[1] = 0
for i in range(1,n+1):
    if i > 1:
        dp[i] = min(dp[i],dp[i-1]+abs(h[i-1]-h[i-2]))
    if i > 2:
        dp[i] = min(dp[i],dp[i-2]+abs(h[i-1]-h[i-3]))


print(dp[n])