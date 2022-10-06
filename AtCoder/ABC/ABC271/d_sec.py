n,s = map(int,input().split())

ab = [map(int, input().split()) for i in range(n)]
a,b = [list(i) for i in zip(*ab)]

dp = [[0]*(10001) for i in range(n+1)]

dp[0][0] = 1
for i in range(n):
    for j in range(s):
        if dp[i][j]:
            if j + a[i] <= s:
                dp[i+1][j+a[i]] = 1
            if j + b[i] <=s:
                dp[i+1][j+b[i]] = 1

if dp[n][s] > 0:
    print("Yes")
    ans = []
    for i in range(n-1,-1,-1):
        if s >= a[i] and dp[i][s-a[i]] > 0:
            ans.append("H")
            s-= a[i]
        else:
            ans.append("T")
            s -= b[i]
    A = ""
    for i in range(len(ans)):
        A+=ans[len(ans)-i-1]
    print(A)
else:
    print("No")
