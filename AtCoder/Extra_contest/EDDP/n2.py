import sys
sys.setrecursionlimit(10**6) 

n = int(input())
a = list(map(int, input().split()))

dp = [[[10**10, 0] for j in range(n+1)] for i in range(n+1)]
def rec(l, r):


    if dp[l][r][0] != 10**10:
        return dp[l][r]
    if r-l == 1:
        return [0, a[l]]
    for i in range(l+1, r):
        x = rec(l, i)
        y = rec(i, r)
        sum = x[1] + y[1]
        cost = x[0] + y[0] + sum
        if dp[l][r][0] > cost:
            dp[l][r] = [cost, sum]

    return dp[l][r]
rec(0, n)

print(dp[0][n][0])


