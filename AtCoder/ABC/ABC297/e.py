n, k = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
dp = [[0]*10**6 for i in range(n+1)]

for i in range(n):

    if i == 0:
        for j in range(k+2):
            dp[i][j] = a[i]*j
    else:
        bef = 1
        top = 0
        
        for j in range(1,k+2):
            flag = 0
            if dp[i-1][bef] < dp[i][top] + a[i] and bef <= k:
                dp[i][j] = dp[i-1][bef]
                flag = 1
                bef += 1
           
            elif dp[i-1][bef] >= dp[i][top] + a[i] :
                dp[i][j] = dp[i][top] + a[i]
                top += 1
            if dp[i][j-1]==dp[i][j]:
                dp[i][j] = dp[i][bef] + a[i]
                if flag == 1:
                    top += 1
                elif bef<k:
                    bef += 1
                    

 

print(dp[n-1][k])