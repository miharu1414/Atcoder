n = int(input())
a = list(map(int,input().split()))

dp = [[[0]*(301) for i in range(301)] for j in range(301)]
flag = [[[0]*(301) for i in range(301)] for j in range(301)]
c1 = 0
c2 = 0
c3 = 0
for i in a:
    if i == 1:
        c1 += 1
    if i == 2:
        c2 += 1
    elif i == 3:
        c3 += 1



dp[0][0][0]=0
flag[0][0][0]=1
def rec(c1 ,c2,c3):
    if flag[c1][c2][c3] ==1:
        return dp[c1][c2][c3]
    dp[c1][c2][c3] = 1/(1-(n-c1-c2-c3)/n)
    if c1>0:
        dp[c1][c2][c3] += rec(c1-1,c2,c3)*c1/n/(1-(n-c1-c2-c3)/n)
    if c2>0:
        dp[c1][c2][c3]  += rec(c1+1,c2-1,c3)*c2/n/(1-(n-c1-c2-c3)/n)
    if c3>0:
        dp[c1][c2][c3]  += rec(c1,c2+1,c3-1)*c3/n/(1-(n-c1-c2-c3)/n)
    flag[c1][c2][c3] = 1 
    return dp[c1][c2][c3] 

print(rec(c1,c2,c3))
