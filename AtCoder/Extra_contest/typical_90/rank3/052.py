from operator import mod


n = int(input())
a = [list(map(int,input().split())) for i in range(n)]


sum = [0]*101
ans = 1
mod = 10**9+7

for i in range(n):
    for j in range(6):
        sum[i]+=a[i][j]

for i in range(n):
    ans *= sum[i]%mod
    ans %= mod


print(ans)
