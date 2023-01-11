for m in range(1,100):
    a = 20
    dp = [0]*(m+1)
    dp[0] = 1
    for i in range(m):
        dp[i+1] = 1 / (1+m/(a*dp[i]))
    print(dp[m])
    if dp[m] <= 0.05:
        print(f"{m}が最小値")
        break