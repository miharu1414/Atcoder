import sys
sys.setrecursionlimit(10 ** 6)
n,s = map(int,input().split())
a,b= [],[]
for i in range(n):
    x,y = map(int,input().split())
    a.append(x)
    b.append(y)

dp = [[0]*(10001) for i in range(n+1)]

dp[0][a[0]] = 1
dp[0][b[0]] = 1
for i in range(n):
    if i == 0:
        continue
    for j in range(10001):
        if j - a[i]>=0:
            dp[i][j] += dp[i-1][j-a[i]]
        if j - b[i]>=0:
            dp[i][j] += dp[i-1][j-b[i]]
if dp[n-1][s] <=0:
    print("No")
    exit()

ans = []
from collections import deque

d = deque()
def rec(now,atai):
    if atai < 0:
        return 
    if now == 0:
        if atai == 0:
            ans = list(d)
            ans.reverse()
            A = ''
            print("Yes")
            for i in ans:
                A += i
            print(A)
            exit()
        else:
            return 

    else:
        d.append('T')
        rec(now-1,atai-a[now-1])
        d.pop()
        d.append('H')
        rec(now-1,atai-b[now-1])
        d.pop()


rec(n,s)
print("No")