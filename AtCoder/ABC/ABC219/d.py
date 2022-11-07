from cmath import inf


n = int(input())
x,y = map(int,input().split())
ab=[map(int,input().split()) for i in range(n)]
a,b = [list(i) for i in zip(*ab)]

if x>sum(a) or y > sum(b):
    print(-1)
    exit()

a_num = [0]*(301)
b_num  = [0]*(301)
for i in range(n):
    a_num[a[i]]+=1
    b_num[b[i]]+=1

dp = [[[inf for i in range(301)]for i in range(301)] for i in range(n+1)]
dp[0][0][0] = 0
for i in range(n):
    for j in range(301):
        for k in range(301):

            dp[i+1][j][k] = min(dp[i+1][j][k],dp[i][j][k])
            if  j + a[i]<=300 and k + b[i]<=300 :
                dp[i+1][j+a[i]][k+b[i]] = min(dp[i+1][j+a[i]][k+b[i]],dp[i][j][k] + 1)
            if j+a[i]>300 and k + b[i] > 300:
                dp[i+1][300][300] = min(dp[i+1][300][300],dp[i][j][k]+1)
            elif j + a[i]>300: 
                dp[i+1][300][k+b[i]] = min(dp[i+1][300][k+b[i]],dp[i][j][k]+1)
            elif k + b[i] >= 300:
                dp[i+1][j+a[i]][300] = min(dp[i+1][j+a[i]][300],dp[i][j][k]+1)          
                
            

ans = inf
for j in range(x,301):
    for k in range(y,301):
        ans = min(ans,dp[n][j][k])
print(ans)
            