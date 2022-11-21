n = int(input())
p = list(map(float,input().split()))

dp = [[0]*3000 for i in range(3000)]


dp[0][0] = 1-p[0]
dp[0][1] = p[0]
for i in range(1,n):
    for j in range(n+1):
        if j>0:
            dp[i][j] += dp[i-1][j-1]*p[i]
        dp[i][j] += dp[i-1][j]*(1-p[i])
sum = 0
for i in range(n//2+1,n+1):
    sum+=dp[n-1][i]
print(sum)