a= list(map(int,input().split()))
dp = dict()
for i in a:
    dp[i] = 1
ans = 0
for i in dp:
    ans += 1
print(ans)