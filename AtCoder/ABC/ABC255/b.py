n, k = map(int,input().split())
a = list(map(int,input().split()))
xy = [list(map(int,input().split())) for i in range(n)]
x,y = [list(i) for i in zip(*xy)]

for i in range(k):
    a[i] -=1
import math

max_dis  = -1
dp = [-1]*n

for i in range(k):
    for j in range(n):
        if a[i] == j :
            dp[j] = 0
        elif dp[j] == -1:
            dp[j] = math.sqrt((x[a[i]]-x[j])**2+(y[a[i]]-y[j])**2)
        else:
            dis = math.sqrt((x[a[i]]-x[j])**2+(y[a[i]]-y[j])**2)
            dp[j] = min(dp[j],dis)
print(max(dp))