n ,x = map(int,input().split())
ab = [map(int,input().split()) for i in range(n)]
a,b = [list(i) for i in zip(*ab)]

num = [0]*101
for i in range(n):
    num[a[i]] = b[i]

dp = [[[0]*(x+1)for i in range(51)] for i in range(101)]
for i in range(n):
    dp[i][0][0] = 1

dp1 = [0]*(10**7)
dp1[0] = 1
dp2 = [[0]*(x+1) for i in range(n+1)]
for i in range(n):
    dp2[i][0] = 1
for i in range(n):
    for j in range(b[i]+1):
        for k in range(x+1):
            if k-a[i]*j >=0 and dp2[i][k-a[i]*j]:
                dp2[i+1][k] |= dp2[i][k-a[i]*j]
if dp2[n][x]:  print("Yes")
else:    print("No")    