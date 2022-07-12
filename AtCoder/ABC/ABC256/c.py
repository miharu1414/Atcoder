

h1,h2,h3, w1,w2,w3 = map(int,input().split())

h = [h1,h2,h3]
w = [w1,w2,w3]



def check(dp):
    for i in range(2):
        dp[i][2] = h[i] - dp[i][0] -dp[i][1]
        if dp[i][2]<1:
            return 0
    for j in range(2):
        dp[2][j] = w[j] - dp[0][j] -dp[1][j]
        if dp[2][j]<1:
            return 0
    if (w[2] - dp[0][2] - dp[1][2] != h[2] -dp[2][0]-dp[2][1]):
        return 0
    elif w[2] - dp[0][2]-dp[1][2] <1:
        return 0
    return 1

    
dp =[[0]*3 for i in range(3)]
ans = 0

for i in range(1,29):
    dp[0][0] = i
    for j in range(1,29):
        if i + j >29:
            break
        dp[0][1] = j
        for k in range(1,29):
            if i + k > 29:
                break
            dp[1][0] = k
            for l in range(1,29):
                if k + l>29:
                    break
                dp[1][1] = l

                ans += check(dp)
print(ans)






