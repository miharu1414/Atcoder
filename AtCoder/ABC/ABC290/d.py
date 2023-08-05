import math
t = int(input())

for i in range(t):
    n, d, k = map(int, input().split())
    d = d % n
    if d == 0:
        d = 1
    groupNum = math.ceil(n/d)
    amari = (k - groupNum) % groupNum

    if amari == 0:
        amari = groupNum
    x = (k-amari)//groupNum
    ans = math.ceil(n/groupNum)*(amari-1) + x
    print(ans)
