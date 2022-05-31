# https://atcoder.jp/contests/typical90/tasks/typical90_bx
n = int(input())
a = list(map(int,input().split()))

dp = [0]*(2*n)
for i in range(n):
    dp[i] = a[i]
    dp[i+n] = a[i]
length = [0]*(2*n+1)
for i in range(len(dp)):
    length[i+1] = length[i] + dp[i]

import bisect

N = sum(a)

for i in range(len(length)):
    left = length[i]
    right_i = bisect.bisect_left(length, left + N/10)
    if right_i >=0 and right_i <len(length) and left+N/10 == length[right_i]:
        print("Yes")
        exit()

print("No")