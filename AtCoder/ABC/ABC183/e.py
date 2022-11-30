h,w = map(int,input().split())

s = [input() for i in range(h)]

dp = [[0]*(w+1) for i in range(h+1)]
right = [0]*(h+1)
sita = [0]*(w+1)
naname = [0]*(2000+w+h+1)
dp[0][0]=  1
mod = 10**9+7
for i in range(h):
    for j in range(w):
        if s[i][j] =='#':
            sita[j] = 0
            right[i] = 0
            naname[i-j+2000] = 0
            continue
        dp[i][j] += sita[j]

        dp[i][j] += right[i]
        
        dp[i][j] += naname[i-j+2000]
        dp[i][j] %= mod
        sita[j] = (sita[j]+dp[i][j])%mod
        right[i] = (right[i]+dp[i][j])%mod
        naname[i-j+2000] = (naname[i-j+2000]+dp[i][j])%mod

print(dp[h-1][w-1])
        