n,m,k = map(int,input().split())


dp = [[0]*2502 for i in range(51)]

for i in range(1,m+1):
    dp[0][i] = 1

for i in range(1,n):
    for j in range(1,k+1):
        for p in range(1,m+1):
            dp[i][j] += dp[i-1][j-p]%998244353
            dp[i][j]%= 998244353
ans = 0
for i in range(k+1):
    ans += dp[n-1][i]%998244353
    ans%=998244353
print(ans)




