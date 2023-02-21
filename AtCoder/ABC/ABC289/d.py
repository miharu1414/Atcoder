n = int(input())
a = list(map(int,input().split()))
m = int(input())
b=  list(map(int,input().split()))
x = int(input())
dame = set(b)
dp = [0]*(x+1)
dp[x] = 1
for i in range(x,-1,-1):
    if i in dame:
        continue
    for j in range(n):
        if i + a[j] <= x:
            dp[i] += dp[i+a[j]]
if dp[0]:
    print("Yes")
else:
    print("No")