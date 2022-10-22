n = int(input())
dp = [[[0]*4 for k in range(10)] for i in range(n+1)]

now = 0
for i in range(10):
    if i != 0 or i != 9:
        dp[0][i][0] = 1
    if i == 0:
        dp[0][i][1] = 1
    if i == 9:
        dp[0][i][2] = 1
    now += 1

mod = 10**9 + 7
for i in range(n-1):
    for j in range(10):
        for k in range(10):

            
            dp[i+1][j][0]%=mod  
            dp[i+1][j][1]%=mod       
            if j == 9:
                dp[i+1][j][2] += dp[i][k][0]
                dp[i+1][j][3] += dp[i][k][1]
                
                dp[i+1][j][2] %= mod
                dp[i+1][j][3] %= mod
            elif j == 0:
                dp[i+1][j][1] += dp[i][k][0]
                dp[i+1][j][3] += dp[i][k][2]  
                dp[i+1][j][1] %=mod
                dp[i+1][j][3] %=mod 
            else:
                dp[i+1][j][0] += dp[i][k][0]
                dp[i+1][j][1] += dp[i][k][1]
                dp[i+1][j][2] += dp[i][k][2]
                dp[i+1][j][3] += dp[i][k][3]
                dp[i+1][j][0] %=mod
                dp[i+1][j][1] %=mod
                dp[i+1][j][2] %=mod
                dp[i+1][j][3] %=mod
                  

                
                   
            
ans = 0
for i in range(10):
    ans = (ans + dp[n-1][i][3])%mod
print(ans)