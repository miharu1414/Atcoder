n = int(input())
a = [list(map(int,input().split())) for i in range(n)]

dp= []
for i in range(n):
    dp.append(sum(a[i]))
ans  = 1
mod = 10**9+7
for i in range(n):
    ans = (ans*dp[i])%mod
print(ans)