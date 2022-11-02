n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

dp = [[0]*(3002) for i in range(n+1)]


for i in range(n):
    a[i]+=1
    b[i]+=1

ruiseki = [0]*(3002)
mod = 998244353
for j in range(1,3002):
    
    if a[0] <= j and j <= b[0]:
        dp[0][j] = 1
    ruiseki[j] = ruiseki[j-1] + dp[0][j]
    ruiseki[j] %= mod
for i in range(1,n):
    
    ruiseki[0] = 0
    for j in range(1,3002):
        if a[i] <= j and j <= b[i] :
            dp[i][j] += ruiseki[j]
            dp[i][j] %= mod
        ruiseki[j] = ruiseki[j-1] + dp[i][j]
        ruiseki[j] %= mod
print(sum(dp[n-1])%mod)