n ,x = map(int,input().split())
xy = [map(int, input().split()) for _ in range(n)]
a, b = [list(i) for i in zip(*xy)]
dp = [[0]*101 for i in range(10001)]
dp[0][0] = 1
for i in range(1,n+1):
    for j in range(x+1):
        if j - a[i-1] < 0:
            pass
        elif dp[i-1][j-a[i-1]] == 1:
            dp[i][j] = 1
        if j - b[i-1] < 0:
            pass
        elif dp[i-1][j-b[i-1]] == 1:
            dp[i][j] = 1
if dp[n][x] == 1:
    print("Yes")
else:
    print("No")