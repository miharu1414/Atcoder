n = int(input())
t  = list(map(int,input().split()))

dp = [[0]*(100001) for i in range(n+1)]
dp[0][0] = 1
for i in range(1,n+1):
    for j in range(100001):
        
        if j - t[i-1] >= 0:
            dp[i][j] += dp[i-1][j-t[i-1]]
        dp[i][j] += dp[i-1][j]
Sum = sum(t)

dif = inf

for i in range(100001):
    if dp[n][i] >= 1:
        dif = min(dif,abs(Sum/2-i))
print(int(Sum/2 + dif))