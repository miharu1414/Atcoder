sagaku = 200000
n,m = map(int,input().split())
a = list(map(int,input().split()))
for i in range(n):
    a[i] = a[i] + sagaku
dp = [[0]*(m+1)for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,min(i+1,m+1)):
        dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]+(j)*a[i-1])
print(int(dp[n][m]-sagaku*m*(m+1)/2))
        
        
    