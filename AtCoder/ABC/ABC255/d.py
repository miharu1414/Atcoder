n,q = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
sum = sum(a)
dp = [0]*(n)
dp[0] = a[0]
for i in range(1,n):
    dp[i] = dp[i-1] + a[i]
import bisect
for i in range(q):
    x = int(input())
    pos_mae = bisect.bisect_left(a,x)
    pos_usiro = bisect.bisect(a,x)
    if x<=a[0]:
        ans1 = 0
    else:
        ans1 = x*pos_mae-dp[pos_mae-1]
    if x>=a[n-1]:
        ans2 = 0
    else:
        if pos_usiro != 0:
            ans2 = dp[n-1] - dp[pos_usiro-1] -x*(n-pos_usiro)
        else:
            ans2 = dp[n-1] -x*(n-pos_usiro)

    print((ans1+ans2))