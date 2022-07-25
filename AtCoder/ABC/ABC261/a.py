l1,r1,l2,r2 = map(int,input().split())
dp = [0]*101
for i in range(l1,r1):
    dp[i] += 1
for i in range(l2,r2):
    dp[i] += 1
cnt = 0
for i in range(0,101):
    if dp[i] == 2:
        cnt += 1
print(cnt)