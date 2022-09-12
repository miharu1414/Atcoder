n = int(input())
a = list(map(int,input().split()))
q = int(input())
b = [int(input()) for i in range(q)]
a.sort()

import bisect
for point in b:
    now = bisect.bisect(a,point)
    if now != 0 and now != n :
        ans = min(abs(a[now-1]-point),abs(a[now]-point))
    elif now == n:
        ans = abs(a[now-1]-point)
    else:
        ans =abs(a[now]-point)
    print(ans)